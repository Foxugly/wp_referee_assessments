from django.shortcuts import render
from django.views.generic import UpdateView
from customuser.models import CustomUser
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from django.contrib.messages.views import SuccessMessageMixin
from customuser.forms import CustomUserForm


class CustomUserUpdateView(SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'update.html'
    success_url = reverse_lazy('update_user')
    success_message = _('Changes saved.')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context
