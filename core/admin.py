from django.contrib import admin
from core import models


class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title']


class PostAdmin(admin.ModelAdmin):
    list_display = ['idea', 'content']


admin.site.register(models.Idea, IdeaAdmin)
admin.site.register(models.Post, PostAdmin)
