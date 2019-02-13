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
from championship.views import home
from assessment.views import evaluation, stats
from users.views import MyUpdateView
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', home, name='home'),
    path('evaluation/<int:match_id>/', evaluation, name="evaluation"),
    path('stats/', stats, name="stats"),
    path('admin/', admin.site.urls),
    path('update/', login_required(MyUpdateView.as_view()), name="update"),
    path('select2/', include('django_select2.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('hijack/', include('hijack.urls', namespace='hijack')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
