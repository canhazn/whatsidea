from django.shortcuts import render
from core import models
from django.http import JsonResponse


# Create your views here.
def upload_image(request):
    img_file = request.FILES["image"]

    image = models.Image.objects.create(
        user=request.user,
        img_file=request.FILES["image"]
    )

    return JsonResponse({
        "success": 1,
        "file": {
            "url": "%s/%s" % ("media", str(image.img_file))
        }
    })


def view_image(request, file_name):
    return JsonResponse({
        "message": "idea created",
    })
