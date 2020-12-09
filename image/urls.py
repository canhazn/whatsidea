from django.urls import path
from image import views


urlpatterns = [
    path("upload/", views.upload_image, name="image-upload-api"),
    path("<str:file_name>/", views.view_image, name="image-view-api")
]
