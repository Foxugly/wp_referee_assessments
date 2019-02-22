"""Customuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import include, path, reverse
from django.utils import timezone, translation

from customuser.decorators import check_lang, superuser_only
from customuser.views import CustomUserUpdateView, home, stats, evaluation


def set_language(request):
    if 'lang' in request.GET and 'next' in request.GET:
        if translation.LANGUAGE_SESSION_KEY in request.session:
            del request.session[translation.LANGUAGE_SESSION_KEY]
        translation.activate(request.GET.get('lang'))
        request.session[translation.LANGUAGE_SESSION_KEY] = request.GET.get('lang')
        return HttpResponseRedirect(request.GET.get('next'))
    else:
        return reverse('home')


urlpatterns = [
    path('',login_required(home), name='home'),
    path('lang/', set_language, name='lang'),
    path('evaluation/<int:am_id>/',login_required(evaluation), name="evaluation"),
    path('stats/',login_required(stats), name="stats"),
    path('admin/', admin.site.urls),
    path('championship/', include('championship.urls', namespace='championship')),
    path('assessment/', include('assessment.urls', namespace='assessment')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/update/', login_required(check_lang(CustomUserUpdateView.as_view())), name='update_user'),
    path('hijack/', include('hijack.urls', namespace='hijack')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [ path('__debug__/', include(debug_toolbar.urls)), ]
