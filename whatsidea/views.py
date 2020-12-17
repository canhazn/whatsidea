from django.shortcuts import render
from core import models
from django.db.models import Q
from django.core.paginator import Paginator


def homePage(request):
    idea_count = models.Idea.objects.all().count()

    query = request.GET.get("search", "")
    idea_list = models.Idea.objects.filter(
        Q(shortdesc__contains=query) | Q(title__contains=query))

    paginator = Paginator(idea_list, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        "idea_count": idea_count,
        "query": query
    }
    return render(request, 'index.html', context)


def privacyPage(request):
    return render(request, 'privacy.html')


def policyPage(request):
    return render(request, 'policy.html')
