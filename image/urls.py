from django.urls import path
from image import views


urlpatterns = [
    path("<int:pk>/", views.view_image, name="image-view-api"),
    path("upload/", views.upload_image, name="image-upload-api")
]
