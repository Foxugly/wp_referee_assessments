from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import MyUser
from .forms import MyUserChangeForm, MyUserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from hijack_admin.admin import HijackUserAdminMixin


class MyUserAdmin(UserAdmin, HijackUserAdminMixin):
	form = MyUserChangeForm
	add_form = MyUserCreationForm
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_referee_admin', 'hijack_field',)
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_referee_admin')
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
		(_('Permissions'), {'fields': ('is_active', 'is_referee_admin', 'is_superuser', 'teams', 'categories')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'password1', 'password2'),
		}),
	)
	search_fields = ('username', 'first_name', 'last_name', 'email')
	ordering = ('username',)
	filter_horizontal = ('teams', 'categories',)


admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)