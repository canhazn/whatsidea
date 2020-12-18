from django.urls import path
from contribution import views


urlpatterns = [
    path("create/", views.contribution_create, name="contribution-create-api"),
    path("delete/", views.contribution_delete, name="contribution-delete-api"),
    path("list-parent-contribution/",
         views.list_parent_contribution, name="api-list-parent-contribution"),
    path("list-sub-contribution/",
         views.list_sub_contribution, name="api-list-sub-contribution"),
]
