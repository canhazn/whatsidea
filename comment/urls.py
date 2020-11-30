from django.urls import path
from comment import views


urlpatterns = [
    path("create/", views.comment_create, name="comment-create-api"),
    path("delete/", views.commnent_delete, name="comment-delete-api")
]