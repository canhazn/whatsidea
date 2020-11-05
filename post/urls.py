from django.urls import path
from post import views

urlpatterns = [
    path("create/", views.post_create, name="post-create-api"),
    path("update/", views.post_update, name="post-update-api"),
    path("delete/", views.post_delete, name="post-delete-api")
]
