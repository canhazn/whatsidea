from django.urls import path
from comment import views


urlpatterns = [
    path("create/", views.comment_create, name="comment-create-api"),
    path("delete/", views.comment_delete, name="comment-delete-api"),
    path("list-parent-comment/",
         views.list_parent_comment, name="api-list-parent-comment"),
    path("list-children-comment/",
         views.list_sub_comment, name="api-list-children-comment"),
]
