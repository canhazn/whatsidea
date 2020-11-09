from django.db import models
from django.contrib.auth.models import User


class Idea(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True)
    problem = models.TextField()
    solution = models.TextField()
    is_publish = models.BooleanField(default=True)
    is_success = models.BooleanField(default=False)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    website = models.CharField(max_length=30, blank=True)
    corver_image = models.ImageField(upload_to="media/", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    class Meta:
        ordering = ["date_created"]


class Contribution(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self", blank=True, null=True, related_name="children", on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)


class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "user:%s  idea:%s" % (str(self.user), str(self.idea))
