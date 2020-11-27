from django.core.exceptions import PermissionDenied
from core import models


def user_is_founder(function):
    def wrap(request, *arg, **kargs):
        idea = models.Idea.objects.get(slug=kargs['slug'])

        if request.user in idea.founder.all():
            return function(request, *arg, **kargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
