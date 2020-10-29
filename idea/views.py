from django.shortcuts import render, get_object_or_404
from core import models


def ideaDetail(request, slug):
    idea = get_object_or_404(models.Idea, slug=slug)
    context = {
        "idea": idea
    }
    return render(request, "idea-detail.html", context)