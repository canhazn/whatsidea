from django.urls import path
from like import views

urlpatterns = [
    path("", views.like, name="like-api")    
]
