from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.forms.models import ModelMultipleChoiceField
from .models import MyUser
from championship.models import Team, Category
from django_select2.forms import Select2MultipleWidget


class MyUserCreationForm(UserCreationForm):
	class Meta:
		model = MyUser
		fields = ("username",)


class MyUserChangeForm(UserChangeForm):
	class Meta:
		model = MyUser
		fields = '__all__'


class MyUserForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(MyUserForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['is_referee_admin'].widget.attrs['readonly'] = True
			self.fields['is_referee_admin'].widget.attrs['disabled'] = 'disabled'
			self.fields['is_superuser'].widget.attrs['readonly'] = True
			self.fields['is_superuser'].widget.attrs['disabled'] = 'disabled'
			self.fields['categories'].widget.attrs['readonly'] = True
			self.fields['categories'].widget.attrs['disabled'] = 'disabled'
			self.fields['teams'].widget.attrs['readonly'] = True
			self.fields['teams'].widget.attrs['disabled'] = 'disabled'
			#for f in self.fields.keys():
			#	self.fields[f].widget.attrs['class'] = "form-control"


	class Meta:
		model = MyUser
		fields = ['username', 'first_name', 'last_name', 'email', 'language', 'is_referee_admin', 'is_superuser', 'categories', 'teams']

	teams = ModelMultipleChoiceField(queryset=Team.objects.all(), widget=Select2MultipleWidget)
	categories = ModelMultipleChoiceField(queryset=Category.objects.all(), widget=Select2MultipleWidget)