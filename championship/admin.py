from django.contrib import admin
from .models import Season, Category, Competition, Team, Referee, Match


# Register your models here.
class SeasonAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class CompetitionAdmin(admin.ModelAdmin):
    pass


class TeamAdmin(admin.ModelAdmin):
    pass


class RefereeAdmin(admin.ModelAdmin):
    pass


class MatchAdmin(admin.ModelAdmin):
    pass


admin.site.register(Season, SeasonAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Referee, RefereeAdmin)
admin.site.register(Match, MatchAdmin)
