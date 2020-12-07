from django.shortcuts import render, redirect, get_object_or_404
from core import models
from django.http import JsonResponse


# Create your views here.
def upload_image(request):
    image = models.Image.objects.create(
        user=request.user,
        img_file=request.FILES["image"]
    )

    print(image.img_file)
    return JsonResponse({
        "success": 1,
        "file": {
            "url": "%s" % (image.img_file)
        }
    })


def view_image(request, file_name):
    img = get_object_or_404(models.Image, img_file="image/%s" % (file_name))
    return redirect(img.img_file.url)
