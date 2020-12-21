from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import json
from core import models
from django.core import serializers
from django.template.loader import render_to_string
from django.core.paginator import Paginator


def list_parent_contribution(request):
    idea_id = request.GET.get('idea_id')
    idea = get_object_or_404(models.Idea, id=idea_id)
    contribution_query = idea.contribution_set.filter(parent__isnull=True)

    paginator = Paginator(contribution_query, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    rended_contribution = render_to_string(
        template_name="contribution/list-contribution.html",
        context={
            "page_obj": page_obj,
        }, request=request
    )

    if page_obj.has_next():
        return JsonResponse({
            "page_number": page_obj.next_page_number(),
            "contribution": rended_contribution
        })
    else:
        return JsonResponse({
            "contribution": rended_contribution
        })


def list_sub_contribution(request):
    parent_id = request.GET.get('parent_id')
    contribution = get_object_or_404(models.Contribution, id=parent_id)
    contribution_query = contribution.children.all()

    paginator = Paginator(contribution_query, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    rended_contribution = render_to_string(
        template_name="contribution/list-children-contribution.html",
        context={
            "page_obj": page_obj,
        }, request=request
    )

    if page_obj.has_next():
        return JsonResponse({
            "page_number": page_obj.next_page_number(),
            "contribution": rended_contribution
        })
    else:
        return JsonResponse({
            "contribution": rended_contribution
        })


@login_required()
def contribution_create(request):

    data = json.loads(request.body)
    idea_id = data["idea_id"]
    content = data["content"]

    if "parent_id" in data:
        parent_id = data["parent_id"]
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
        template_name="contribution/contribution.html",
        context={
            "contribution": contribution
        },
        request=request
    )

    print("contribution created: ", contribution)

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
