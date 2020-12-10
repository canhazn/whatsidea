from django.shortcuts import render
from core import models
from django.db.models import Q


def homePage(request):
    idea_count = models.Idea.objects.all().count()
    query = request.GET.get("search", "")
    print(query)
    
    ideas = models.Idea.objects.filter(Q(shortdesc__contains=query) | Q(title__contains=query))[:2]
    # ideas = models.Idea.objects.all().order_by('-id')[:5]
    print(ideas)
    context = {
        "ideas": ideas,
        "idea_count": idea_count
    }
    return render(request, 'index.html', context)


def privacyPage(request):
    return render(request, 'privacy.html')


def policyPage(request):
    return render(request, 'policy.html')
