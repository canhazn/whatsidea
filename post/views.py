from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from core import models, forms
import json


@login_required()
def post_create(request):

    data = json.loads(request.body)
    print(request.body)
    content = data["content"]
    user = request.user
    idea_id = data['idea_id']
    idea = models.Idea.objects.get(id=idea_id)
    
    post = models.Post.objects.create(
        user=user,
        idea=idea,
        content=content
    )

    return JsonResponse({
        "message": "post created"
    })


@login_required()
def post_delete(request):

    data = json.loads(request.body)
    print("------------------", data)
    post_id = data["post_id"]

    post = get_object_or_404(models.Post, id=post_id)
    post.delete()
    return JsonResponse({
        "message": "post deleted"
    })


@login_required()
def post_update(request):

    data = json.loads(request.body)
    print("------------------", data)
    post_id = data["post_id"]
    content = data["content"]

    post = get_object_or_404(models.Post, id=post_id)
    post.content = content

    post.save()
    return JsonResponse({
        "message": "post update"
    })
