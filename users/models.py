from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from championship.models import Team, Category
from settings import LANGUAGES


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    language = models.CharField(_("language"), max_length=8, choices=LANGUAGES, default=1)
    teams = models.ManyToManyField(Team, blank=True, verbose_name=_('teams'))
    categories = models.ManyToManyField(Category, blank=True, verbose_name=_('categories'))
    is_referee_admin = models.BooleanField(_("Referee admin"), default=False, help_text=_('Designates users that can access to statistics.'),)
    objects = CustomUserManager()

    def get_teams(self):
        return self.teams.all()

    def get_categories(self):
    	return self.categories.all()

    def __str__(self):
    	return self.username