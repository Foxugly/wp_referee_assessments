from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from championship.models import Team, Category
from settings import LANGUAGES


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password):
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    language = models.CharField(_("language"), max_length=8, choices=LANGUAGES, default=1)
    teams = models.ManyToManyField(Team, blank=True, verbose_name=_('teams'))
    categories = models.ManyToManyField(Category, blank=True, verbose_name=_('categories'))
    is_referee_admin = models.BooleanField(_("Referee admin"), default=False, help_text=_('Designates users that can access to statistics.'),)
    
    USERNAME_FIELD = 'username'

    def get_teams(self):
        return self.teams.all()

    def get_categories(self):
    	return self.categories.all()

    def __str__(self):
    	return self.username
