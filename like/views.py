from django.shortcuts import get_object_or_404
from core import models
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import JsonResponse
import json


@login_required
def like(request):
    data = json.loads(request.body)
    if data["post_id"]:
        post_id = data["post_id"]
        post = get_object_or_404(models.Post, id=post_id)
        like, created_post = models.Like.objects.get_or_create(user=request.user, post=post,)
        if not created_post:
            like.delete()
            return JsonResponse({
                "message": "like deleted"
            })
        else:
            return JsonResponse({
                "message": "like created"
            })
    elif data["comment_id"]:
        comment_id = data["comment_id"]
        comment = get_object_or_404(models.Comment, id=comment_id)
        like, created_comment = models.Like.objects.get_or_create(user=request.user, comment=comment)
        if not created_comment:
            like.delete()
            return JsonResponse({
                "message": "like created"
            })
        else:
            return JsonResponse({
                "message": "like created"
            })

    