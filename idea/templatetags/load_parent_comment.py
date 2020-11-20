from django import template

register = template.Library()


@register.filter
def load_parent_comment(comments):    
    return comments.filter(parent__isnull=True)
