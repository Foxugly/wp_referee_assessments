from championship.views import SeasonListView, SeasonUpdateView, SeasonDetailView, SeasonCreateView, TeamListView, TeamUpdateView, TeamDetailView, TeamCreateView, CategoryListView, CategoryUpdateView, CategoryDetailView, CategoryCreateView, CompetitionListView, CompetitionUpdateView, CompetitionDetailView, CompetitionCreateView, RefereeListView, RefereeUpdateView, RefereeDetailView, RefereeCreateView, MatchListView, MatchUpdateView, MatchDetailView, MatchCreateView

from django.urls import path


app_name = 'championship'
urlpatterns = [
	path('season/', SeasonListView.as_view(), name='season_list'),
	path('season/add/', SeasonCreateView.as_view(), name="season_add"),
	path('season/<int:pk>/', SeasonDetailView.as_view(), name="season_detail"),
	path('season/<int:pk>/change/', SeasonUpdateView.as_view(), name="season_change"),

	path('team/', TeamListView.as_view(), name='team_list'),
	path('team/add/', TeamCreateView.as_view(), name="team_add"),
	path('team/<int:pk>/', TeamDetailView.as_view(), name="team_detail"),
	path('team/<int:pk>/change/', TeamUpdateView.as_view(), name="team_change"),

	path('category/', CategoryListView.as_view(), name='category_list'),
	path('category/add/', CategoryCreateView.as_view(), name="category_add"),
	path('category/<int:pk>/', CategoryDetailView.as_view(), name="category_detail"),
	path('category/<int:pk>/change/', CategoryUpdateView.as_view(), name="category_change"),

	path('competition/', CompetitionListView.as_view(), name='competition_list'),
	path('competition/add/', CompetitionCreateView.as_view(), name="competition_add"),
	path('competition/<int:pk>/', CompetitionDetailView.as_view(), name="competition_detail"),
	path('competition/<int:pk>/change/', CompetitionUpdateView.as_view(), name="competition_change"),

	path('referee/', RefereeListView.as_view(), name='referee_list'),
	path('referee/add/', RefereeCreateView.as_view(), name="referee_add"),
	path('referee/<int:pk>/', RefereeDetailView.as_view(), name="referee_detail"),
	path('referee/<int:pk>/change/', RefereeUpdateView.as_view(), name="referee_change"),

	path('match/', MatchListView.as_view(), name='match_list'),
	path('match/add/',MatchCreateView.as_view(), name="match_add"),
	path('match/<int:pk>/', MatchDetailView.as_view(), name="match_detail"),
	path('match/<int:pk>/change/', MatchUpdateView.as_view(), name="match_change"),
]