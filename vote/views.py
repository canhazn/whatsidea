from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from core import models


@login_required()
def vote(request, slug):

    idea = get_object_or_404(models.Idea, slug=slug)

    vote, created = models.Vote.objects.get_or_create(
        user=request.user, idea=idea)

    if not created:        
        vote.delete()
        return JsonResponse({
            "message": "vote deleted"
        })
    else:
        return JsonResponse({
            "message": "vote created"
        })
        

