from django.contrib import admin
from core import models


class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_owners']

    def get_owners(self, obj):
        return ",".join([str(user) for user in obj.user.all()])

    get_owners.short_description = "owner"


class PostAdmin(admin.ModelAdmin):
    list_display = ['idea', 'content']


class ContributeAdmin(admin.ModelAdmin):
    list_display = ['user', 'idea', 'parent', 'content']


class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'idea', 'date_created']


admin.site.register(models.Idea, IdeaAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Contribute, ContributeAdmin)
admin.site.register(models.Vote, VoteAdmin)
