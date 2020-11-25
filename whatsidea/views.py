from django.shortcuts import render
from core import models


def homePage(request):
    idea_count = models.Idea.objects.all().count()
    ideas = models.Idea.objects.all().order_by('-id')[:5]

    context = {
        "ideas": ideas,
        "idea_count": idea_count
    }
    return render(request, 'index.html', context)
