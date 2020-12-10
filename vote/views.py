from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from core import models
from django.core import serializers

import json


@login_required()
def vote(request):
    data = json.loads(request.body)
    print(data)
    if "idea_id" in data:
        idea_id = data["idea_id"]
        idea = get_object_or_404(models.Idea, id=idea_id)
        vote, created_idea = models.Vote.objects.get_or_create(
            user=request.user, idea=idea)
        if not created_idea:
            vote.delete()
            context = {
                "message": "vote deleted"
            }
        else:
            context = {
                "message": "vote created",
                "idea_id": idea.id
            }

    elif "contribution_id" in data:
        contribution_id = data["contribution_id"]
        contribution = get_object_or_404(
            models.Contribution, id=contribution_id)

        vote, created_contribution = models.Vote.objects.get_or_create(
            user=request.user, contribution=contribution)

        if not created_contribution:
            vote.delete()
            context = {
                "message": "vote deleted"
            }
        else:
            context = {
                "message": "vote created",
                "contribution_id": contribution.id
            }
    else:
        context = {
            "message": "id required"
        }

    return JsonResponse(context)
