from django.contrib import admin
from core import models


class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_owners']

    def get_owners(self, obj):
        return ",".join([str(user) for user in obj.founder.all()])

    get_owners.short_content = "owner"


class PostAdmin(admin.ModelAdmin):
    list_display = ['idea', 'content']


class ContributionAdmin(admin.ModelAdmin):
    list_display = ['user', 'idea', 'parent', 'content']


class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'idea', 'date_created']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'content', 'parent']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'bio']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', "date_created"]


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']


admin.site.register(models.Idea, IdeaAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Contribution, ContributionAdmin)
admin.site.register(models.Vote, VoteAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Like, LikeAdmin)
