from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Season(models.Model):
    name = models.CharField(_('name'), max_length=100)
    active = models.BooleanField(_('active'), default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('championship:season_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('championship:season_add')

    def get_detail_url(self):
        return reverse('championship:season_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('championship:season_delete', kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('championship:season_list')

    class Meta:
        verbose_name = _('Season')


class Team(models.Model):
    name = models.CharField(_('name'), max_length=100)
    active = models.BooleanField(_('active'), default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('championship:team_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('championship:team_add')

    def get_detail_url(self):
        return reverse('championship:team_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('championship:team_delete', kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('championship:team_list')

    class Meta:
        verbose_name = _('Team')


class Category(models.Model):
    name = models.CharField(_('name of category'), max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('championship:category_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('championship:category_add')

    def get_detail_url(self):
        return reverse('championship:category_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('championship:category_delete', kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('championship:category_list')

    class Meta:
        verbose_name = _('Category')


class Competition(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name=_('season'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))
    teams = models.ManyToManyField(Team, blank=True, verbose_name=_('teams'))

    def __str__(self):
        return "%s - %s" % (self.season, self.category)

    def get_absolute_url(self):
        return reverse('championship:competition_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('championship:competition_add')

    def get_detail_url(self):
        return reverse('championship:competition_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('championship:competition_delete', kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('championship:competition_list')

    class Meta:
        verbose_name = _('Competition')


class Referee(models.Model):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_absolute_url(self):
        return reverse('championship:referee_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('championship:referee_add')

    def get_detail_url(self):
        return reverse('championship:referee_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('championship:referee_delete', kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('championship:referee_list')

    class Meta:
        verbose_name = _('Referee')


class Match(models.Model):
    datetime = models.DateTimeField(_('datetime of the match'))
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, verbose_name=_('competition'))
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
        return '[%s] %s : %s - %s' % (self.competition, self.datetime, self.teamH, self.teamA)

    def get_absolute_url(self):
        return reverse('championship:match_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('championship:match_add')

    def get_detail_url(self):
        return reverse('championship:match_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('championship:match_delete', kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('championship:match_list')

    class Meta:
        verbose_name = _('Match')
