from django.shortcuts import render, redirect, get_object_or_404
from core import models
from django.http import JsonResponse


# Create your views here.
def upload_image(request):
    img_file = request.FILES["image"]

    image = models.Image.objects.create(
        user=request.user,
        img_file=request.FILES["image"]
    )

    print(image.img_file)
    return JsonResponse({
        "success": 1,
        "file": {
            "url": "%s/%s" % ("image/", str(image.id))
        }
    })


def view_image(request, pk):
    img = get_object_or_404(models.Image, id=pk)
    return redirect(img.img_file.url)
