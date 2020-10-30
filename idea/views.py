from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core import models, forms


@login_required()
def ideaCreate(request):
    if request.method == "POST":
        form = forms.IdeaForm(data=request.POST)
        if form.is_valid():
            idea = form.save()
            idea.user.add(request.user)
            return redirect("idea-detail-page", slug=idea.slug)
            
    context = {
        "form": forms.IdeaForm
    }

    return render(request, "idea-create.html", context)


def ideaDetail(request, slug):
    idea = get_object_or_404(models.Idea, slug=slug)
    contributes = idea.contribute_set.filter(parent__isnull=True)
    # contributes = models.Contribute.objects.filter(parent__isnull=True)

    context = {
        "idea": idea,
        "contributes": contributes
    }
    return render(request, "idea-detail.html", context)
