from django.shortcuts import render
from users.models import MyUser
from django.views.generic import UpdateView


# Create your views here.


class MyUpdateView(UpdateView):
	model = MyUser
	fields = ['username', 'first_name', 'last_name', 'email', 'language']
	template_name = 'registration/profile.html'
	success_url = '/'

	def get_object(self):
		return self.request.user