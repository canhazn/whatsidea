from django.urls import path
from idea import views


urlpatterns = [
    path("create/", views.ideaCreate, name="idea-create-page"),
    path("<slug:slug>/", views.ideaDetail, name="idea-detail-page"),
]
