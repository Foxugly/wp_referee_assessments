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
from django.contrib import admin
from django.urls import include, path
from users.views import CustomUserUpdateView, home, evaluation, stats
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(home), name='home'),
    path('evaluation/<int:match_id>/',login_required(evaluation), name="evaluation"),
    path('stats/',login_required(stats), name="stats"),
    path('admin/', admin.site.urls),
    path('championship/', include('championship.urls', namespace='championship')),
    path('assessment/', include('assessment.urls', namespace='assessment')),
    path('update/', login_required(CustomUserUpdateView.as_view()), name="update"),

    path('i18n/', include('django.conf.urls.i18n')),
    path('select2/', include('django_select2.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('hijack/', include('hijack.urls', namespace='hijack')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
