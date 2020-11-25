from django.urls import path
from comment import views


urlpatterns = [
    path("create/", views.comment_create, name="comment-create-api"),
    # path("delete/", views.contribution_delete, name="contribution-delete-api")
]