from django.urls import path
from idea import views


urlpatterns = [
    path("create/", views.idea_create, name="idea-create-page"),
    path("update/<slug:slug>/", views.idea_update, name="idea-update-page"),    
    path("delete/<slug:slug>/", views.idea_delete, name="idea-delete-page"),
    path("<slug:slug>/", views.idea_detail, name="idea-detail-page"),
]
