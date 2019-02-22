from django.utils import translation
from django.conf import settings

from django.core.exceptions import PermissionDenied
from assessment.models import AssessmentMatch


def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied           
        return function(request, *args, **kwargs)
    return _inner


def user_can_access(function):
    def wrap(request, *args, **kwargs):
        am = AssessmentMatch.objects.get(pk=kwargs['am_id'])
        can = False
        for userteam in request.user.get_teams():
            can = can or (userteam == am.team)
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


def check_lang(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if translation.LANGUAGE_SESSION_KEY in request.session:
                del request.session[translation.LANGUAGE_SESSION_KEY]
                translation.activate(request.user.language)
                request.session[translation.LANGUAGE_SESSION_KEY] = request.user.language
        elif translation.LANGUAGE_SESSION_KEY not in request.session:
            translation.activate(settings.LANGUAGE_CODE)
            request.session[translation.LANGUAGE_SESSION_KEY] = settings.LANGUAGE_CODE
        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
