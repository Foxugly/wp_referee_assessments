from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from customuser.models import CustomUser
from django.forms.models import ModelMultipleChoiceField
from championship.models import Team, Category
#from django_select2.forms import Select2MultipleWidget


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['is_staff'].widget.attrs['readonly'] = True
            self.fields['is_staff'].widget.attrs['disabled'] = 'disabled'
            self.fields['is_referee_admin'].widget.attrs['readonly'] = True
            self.fields['is_refere_admin'].widget.attrs['disabled'] = 'disabled'
            self.fields['is_superuser'].widget.attrs['readonly'] = True
            self.fields['is_superuser'].widget.attrs['disabled'] = 'disabled'
            self.fields['teams'].widget.attrs['readonly'] = True
            self.fields['teams'].widget.attrs['disabled'] = 'disabled'
            self.fields['categories'].widget.attrs['readonly'] = True
            self.fields['categories'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'language', 'is_staff', 'is_referee_admin', 'is_superuser', 'categories', 'teams', ]

#    teams = ModelMultipleChoiceField(queryset=Team.objects.all(), widget=Select2MultipleWidget)
#    categories = ModelMultipleChoiceField(queryset=Category.objects.all(), widget=Select2MultipleWidget)
