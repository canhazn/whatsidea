from core import models
import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


@login_required()
def comment_create(request):
    data = json.loads(request.body)
    post_id = data["post_id"]
    content = data["content"]

    if "parent_id" in data:
        parent_id = data["parent_id"]
        print(parent_id)
        parent = models.Comment.objects.get(id=parent_id)
    else:
        parent = None

    post = models.Post.objects.get(id=post_id)
    models.Comment.objects.create(user=request.user,
                                  post=post,
                                  parent=parent,
                                  content=content)

    return JsonResponse({"message": "comment create"})


@login_required
def commnent_delete(request):
    data = json.loads(request.body)
    comment_id = data["comment_id"]
    comment = get_object_or_404(models.Comment, id=comment_id)
    comment.delete()

    return JsonResponse({"message": "comment deleted"})
