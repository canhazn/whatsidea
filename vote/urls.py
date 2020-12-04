from django.urls import path
from vote import views

urlpatterns = [
    path("", views.vote, name="vote-api")    
]
