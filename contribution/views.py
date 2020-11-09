from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from core import models


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

    return JsonResponse({"message": "contributeion created"})


@login_required()
def contribution_delete(request):

    data = json.loads(request.body)
    contribution_id = data["contribution_id"]
    
    contribution = get_object_or_404(models.Contribution, id= contribution_id)
    contribution.delete()

    return JsonResponse({"message": "contributeion deleted"})

