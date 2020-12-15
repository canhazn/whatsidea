from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import json
from core import models
from django.core import serializers
from django.template.loader import render_to_string


@login_required()
def contribution_create(request):

    data = json.loads(request.body)
    idea_id = data["idea_id"]
    content = data["content"]

    if "parent_id" in data:
        parent_id = data["parent_id"]
        print(parent_id)
        parent = models.Contribution.objects.get(id=parent_id)
    else:
        parent = None

    idea = models.Idea.objects.get(id=idea_id)
    contribution = models.Contribution.objects.create(
        user=request.user,
        idea=idea,
        parent=parent,
        content=content
    )

    rended_contribution = render_to_string(
        template_name="idea/component/contribution.html",
        context={
            "contribution": contribution
        },
        request=request
    )

    return JsonResponse({
        "message": "contribution created",
        "contribution": rended_contribution
    })


@login_required()
def contribution_delete(request):

    data = json.loads(request.body)
    contribution_id = data["contribution_id"]

    contribution = get_object_or_404(models.Contribution, id=contribution_id)
    contribution.delete()

    return JsonResponse({
        "message": "contribution deleted",
        "contribution": {
            "id": contribution.id,
        }
    })
