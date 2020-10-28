from django.db import models
from django.contrib.auth.models import User

class Idea(models.Model):
    title = models.CharField(max_length=500)
    username = models.TextField(max_length=50, blank=True)
    problem = models.TextField()
    solution = models.TextField()
    is_publish = models.BooleanField(default=True)
    is_success = models.BooleanField(default=False)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=12, blank=True)
    website = models.TextField(max_length=30, blank=True)
    corver_image = models.ImageField(upload_to="media/", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    user =  models.ForeignKey(User, null=False ,on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

