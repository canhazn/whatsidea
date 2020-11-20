from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core import models, forms
from django.utils.text import slugify
import json


@login_required()
def idea_create(request):

    # title = data["title"]
    # problem = data["problem"]
    # solution = daat["solution"]

    if request.method == "POST":
        data = json.loads(request.body)
        print("Data: ", request.body)
        print("Body: ", request.body)
        print("Post: ", request.POST)
        form = forms.IdeaCreateForm(data=request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.slug = slugify(idea.title)
            idea.save()
            idea.founder.add(request.user)
            print(idea)
            return redirect("idea-detail-page", slug=idea.slug)
        else:
            print(form.errors)
    context = {
        "form": forms.IdeaCreateForm
    }

    return render(request, "idea/idea-create.html", context)


@login_required()
def idea_update(request, slug):

    idea = get_object_or_404(models.Idea, slug=slug)

    if request.method == "POST":
        idea_form = forms.IdeaForm(request.POST, instance=idea)
        if idea_form.is_valid():
            idea_form.save()
            return redirect("idea-detail-page", slug=idea.slug)
    else:
        idea_form = forms.IdeaForm(instance=idea)

    context = {
        "form": idea_form
    }

    return render(request, "idea/idea-update.html", context)


@login_required()
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
