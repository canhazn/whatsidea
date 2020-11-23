from django.shortcuts import render
from core import models


def homePage(request):
    # ideas = models.Idea.objects.all()
    ideas = models.Idea.objects.all().order_by('-id')[:5]
    context = {
        "ideas": ideas
    }
    return render(request, 'index.html', context)
