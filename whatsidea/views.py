from django.shortcuts import render
from core import models


def homePage(request):
    ideas = models.Idea.objects.all()
    context = {
        "ideas": ideas
    }
    return render(request, 'index.html', context)
