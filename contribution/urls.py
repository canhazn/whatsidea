from django.urls import path
from contribution import views


urlpatterns = [
    path("create/", views.contribution_create, name="contribution-create-api"),
    path("delete/", views.contribution_delete, name="contribution-delete-api")
]
