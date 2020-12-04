from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from core import models
import json


@login_required()
def vote(request):
    data = json.loads(request.body)
    if "idea_id" in data:   
        idea_id = data["idea_id"]
        idea = get_object_or_404(models.Idea, id=idea_id)
        vote, created_idea = models.Vote.objects.get_or_create(user=request.user, idea=idea)
        if not created_idea:
            vote.delete()
            return JsonResponse({
                "message": "vote deleted"
            })
        else:
            return JsonResponse({
                "message": "vote create"
            })
    elif "contribution_id" in data:
        contribution_id = data["contribution_id"]
        contribution = get_object_or_404(models.Contribution, id=contribution_id)
        vote, created_contribution = models.Vote.objects.get_or_create(
        user=request.user, contribution=contribution)

        if not created_contribution:
            vote.delete()
            return JsonResponse({
                "message": "vote deleted"
            })
        else:
            return JsonResponse({
                "message": "vote created"
            })

    return JsonResponse({
                "message": "id required!"
            })
