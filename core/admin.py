from django.contrib import admin
from core import models
from django.utils.html import format_html


class IdeaAdmin(admin.ModelAdmin):
    list_display = ["id", 'title', 'get_owners']

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
    list_display = ['user', "date_created", "image_tag"]

    def image_tag(self, obj):
        return format_html('<img style="max-width: 150px" src="{}"/>'.format(obj.img_file.url))

    image_tag.short_description = "Image"


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'post']


admin.site.register(models.Idea, IdeaAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Contribution, ContributionAdmin)
admin.site.register(models.Vote, VoteAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Like, LikeAdmin)
