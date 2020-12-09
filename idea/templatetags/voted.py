from django import template

register = template.Library()


@register.filter
def voted(contributions, user):
    for contribution in contributions:
        if contribution.user == user:
            return "btn-link"
    return ""
