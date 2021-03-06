from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core import models, forms, decorators
from django.utils.text import slugify
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.core import serializers


@login_required
@require_POST
def idea_create(request):
    data = json.loads(request.body)
    title = data["title"]
    shortdesc = data["shortdesc"]
    content = data["content"]
    slug = slugify(title)

    if not title:
        return JsonResponse({
            "message": "title required",
        })

    from django.db.utils import IntegrityError
    try:
        idea = models.Idea.objects.create(
            title=title,
            shortdesc=shortdesc,
            content=content,
            slug=slug
        )
    except IntegrityError:
        import uuid
        new_slug = "%s-%s" % (slug, uuid.uuid1())
        idea = models.Idea.objects.create(
            title=title,
            shortdesc=shortdesc,
            content=content,
            slug=new_slug
        )

    idea.founder.add(request.user)
    json_content = json.loads(content)

    for block in json_content["blocks"]:
        if block["type"] == "image":
            img_file_name = block["data"]["file"]["url"]
            if img_file_name != "image/man-rocket.png":                
                query_img = get_object_or_404(
                    models.Image, img_file="%s" % (img_file_name))
                query_img.idea = idea
                query_img.save()

    return JsonResponse({
        "message": "idea created",
        "idea_slug": idea.slug
    })


@login_required
@decorators.user_is_founder
def idea_update(request, slug):

    print(slug)
    idea = get_object_or_404(models.Idea, slug=slug)
    if request.method == "POST":
        data = json.loads(request.body)
        idea.title = data["title"]
        idea.shortdesc = data["shortdesc"]
        idea.content = data["content"]
        idea.slug = data["slug"]
        idea.website = data["website"]

        from django.db.utils import IntegrityError
        try:
            idea.save()
        except IntegrityError:
            import uuid
            new_slug = "%s-%s" % (idea.slug, uuid.uuid1())
            idea.slug = new_slug
            idea.save()

        return JsonResponse({
            "message": "idea updated",
            "idea_slug": idea.slug
        })

    else:
        idea_form = forms.IdeaEditForm(instance=idea)
        context = {
            "form": idea_form
        }
        return render(request, "idea/idea-update.html", context)


@login_required
@decorators.user_is_founder
def idea_delete(request, slug):

    idea = get_object_or_404(models.Idea, slug=slug)
    if request.method == "POST":
        idea.delete()
        return redirect('home-page')

    context = {
        "idea": idea
    }
    return render(request, "idea/idea-delete.html", context)


def idea_detail(request, slug):
    idea = get_object_or_404(models.Idea, slug=slug)
    contributions = idea.contribution_set.filter(parent__isnull=True)

    context = {
        "idea": idea,
        "contributions": contributions
    }
    return render(request, "idea/idea-detail.html", context)
