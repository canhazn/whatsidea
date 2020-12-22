from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import json
from core import models
from django.core import serializers
from django.template.loader import render_to_string
from django.core.paginator import Paginator


def list_parent_comment(request):
    post_id = request.GET.get('post_id')
    post = get_object_or_404(models.Post, id=post_id)
    comment_query = post.comment_set.filter(parent__isnull=True)
    print(post)

    paginator = Paginator(comment_query, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    rended_comment = render_to_string(
        template_name="comment/list-comment.html",
        context={
            "page_obj": page_obj,
        }, request=request
    )

    if page_obj.has_next():
        return JsonResponse({
            "page_number": page_obj.next_page_number(),
            "comment": rended_comment
        })
    else:
        return JsonResponse({
            "comment": rended_comment
        })


def list_sub_comment(request):
    parent_id = request.GET.get('parent_id')
    comment = get_object_or_404(models.Comment, id=parent_id)
    comment_query = comment.children.all()

    paginator = Paginator(comment_query, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    rended_comment = render_to_string(
        template_name="comment/list-children-comment.html",
        context={
            "page_obj": page_obj,
        }, request=request
    )

    if page_obj.has_next():
        return JsonResponse({
            "page_number": page_obj.next_page_number(),
            "comment": rended_comment
        })
    else:
        return JsonResponse({
            "comment": rended_comment
        })


@login_required()
def comment_create(request):

    data = json.loads(request.body)
    post_id = data["post_id"]
    content = data["content"]

    if "parent_id" in data:
        parent_id = data["parent_id"]
        parent = models.Comment.objects.get(id=parent_id)
    else:
        parent = None

    post = models.Post.objects.get(id=post_id)
    comment = models.Comment.objects.create(
        user=request.user,
        post=post,
        parent=parent,
        content=content
    )

    rended_comment = render_to_string(
        template_name="comment/comment.html",
        context={
            "comment": comment
        },
        request=request
    )

    print("comment created: ", comment)

    return JsonResponse({
        "message": "comment created",
        "comment": rended_comment
    })


@login_required()
def comment_delete(request):

    data = json.loads(request.body)
    comment_id = data["comment_id"]

    comment = get_object_or_404(models.Comment, id=comment_id)
    comment.delete()

    return JsonResponse({
        "message": "comment deleted",
        "comment": {
            "id": comment.id,
        }
    })
