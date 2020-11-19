from django.contrib import admin
from core import models


class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_owners']

    def get_owners(self, obj):
        return ",".join([str(user) for user in obj.user.all()])

    get_owners.short_description = "owner"


class PostAdmin(admin.ModelAdmin):
    list_display = ['idea', 'content']


class ContributionAdmin(admin.ModelAdmin):
    list_display = ['user', 'idea', 'parent', 'content']


class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'idea', 'date_created']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'bio', 'birth_date']


admin.site.register(models.Idea, IdeaAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Contribution, ContributionAdmin)
admin.site.register(models.Vote, VoteAdmin)
admin.site.register(models.Profile, ProfileAdmin)
