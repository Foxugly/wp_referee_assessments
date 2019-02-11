from django.db import models
from django.utils.translation import gettext_lazy as _


class Team(models.Model):
    name = models.CharField(_('name'), max_length=100)
    active = models.BooleanField(_('active'), default=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(_('name of category'), max_length=20)
    teams = models.ManyToManyField(Team, blank=True, verbose_name=_('teams'))

    def __str__(self):
        return self.name

class Referee(models.Model):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


class Match(models.Model):
    datetime = models.DateTimeField(_('datetime of the match'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))
    teamH = models.ForeignKey(Team, related_name="teamH", on_delete=models.CASCADE, verbose_name=_('team Home'))
    teamA = models.ForeignKey(Team, related_name="teamA",on_delete=models.CASCADE, verbose_name=_('team Away'))
    teams = models.ManyToManyField(Team, related_name="teams", blank=True, verbose_name=_('teams'))
    referees = models.ManyToManyField(Referee, blank=True, verbose_name=_('referees'))

    def get_teams(self):
        return self.teams.all()

    def get_teams_s(self):
        return [t.name for t in self.teams.all()]
    
    def get_referees_s(self):
        return [r.name for r in self.referees.all()]

    def get_referees(self):
        return self.referees.all()
    
    def __str__(self):
        return '[%s] %s : %s' % (self.category, self.datetime, list(self.get_teams_s()))