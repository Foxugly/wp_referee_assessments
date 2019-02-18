from django.core.exceptions import PermissionDenied
from assessment.models import Match


def user_can_access(function):
    def wrap(request, *args, **kwargs):
        m = Match.objects.get(pk=kwargs['match_id'])
        can = False
        for userteam in request.user.get_teams():
            can = can or (userteam in m.get_teams())
        if can:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def referee_admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_referee_admin or request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap