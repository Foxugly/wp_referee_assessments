from django.shortcuts import render
from users.models import MyUser
from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import MyUserForm
from django.utils.translation import gettext_lazy as _
# Create your views here.


class MyUpdateView(SuccessMessageMixin, UpdateView):
	model = MyUser
	template_name = 'registration/profile.html'
	form_class = MyUserForm
	success_url = '/update/'
	success_message = _('Changes saved.')

	def form_valid(self, form):
		return super().form_valid(form)

	def get_object(self):
		return self.request.user