from django import template

register = template.Library()


@register.filter(name='load_parent_comment')
def load_parent_comment(comment):
    return comment.filter(parent=None)
