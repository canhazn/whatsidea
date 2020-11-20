from core import models
import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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
