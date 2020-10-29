from django.urls import path
from idea import views


urlpatterns = [
    path("<slug:slug>/", views.ideaDetail, name="idea-detail-page")
]
