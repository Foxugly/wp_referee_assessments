from django.contrib import admin
from .models import Category, Team, Referee, Match


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	pass

class TeamAdmin(admin.ModelAdmin):
	pass

class RefereeAdmin(admin.ModelAdmin):
	pass

class MatchAdmin(admin.ModelAdmin):
	pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Referee, RefereeAdmin)
admin.site.register(Match, MatchAdmin)