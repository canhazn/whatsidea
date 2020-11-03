from django.urls import path
from vote import views

urlpatterns = [
    path("<slug:slug>/", views.vote, name="vote-api")    
]
