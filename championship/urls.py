from championship.views import SeasonListView, SeasonUpdateView, SeasonDetailView, SeasonCreateView, TeamListView, TeamUpdateView, TeamDetailView, TeamCreateView, CategoryListView, CategoryUpdateView, CategoryDetailView, CategoryCreateView, CompetitionListView, CompetitionUpdateView, CompetitionDetailView, CompetitionCreateView, RefereeListView, RefereeUpdateView, RefereeDetailView, RefereeCreateView, MatchListView, MatchUpdateView, MatchDetailView, MatchCreateView, SeasonDeleteView, TeamDeleteView, CategoryDeleteView, CompetitionDeleteView, RefereeDeleteView, MatchDeleteView
from customuser.decorators import superuser_only
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'championship'
urlpatterns = [
    path('season/', login_required(superuser_only(SeasonListView.as_view())),
         name='season_list'),
    path('season/add/', login_required(superuser_only(SeasonCreateView.as_view())),
         name="season_add"),
    path('season/<int:pk>/',
         login_required(superuser_only(SeasonDetailView.as_view())), name="season_detail"),
    path('season/<int:pk>/change/',
         login_required(superuser_only(SeasonUpdateView.as_view())), name="season_change"),
    path('season/<int:pk>/delete/',
         login_required(superuser_only(SeasonDeleteView.as_view())), name="season_delete"),

    path('team/', login_required(superuser_only(TeamListView.as_view())),
         name='team_list'),
    path('team/add/', login_required(superuser_only(TeamCreateView.as_view())), name="team_add"),
    path('team/<int:pk>/',
         login_required(superuser_only(TeamDetailView.as_view())), name="team_detail"),
    path('team/<int:pk>/change/',
         login_required(superuser_only(TeamUpdateView.as_view())), name="team_change"),
    path('team/<int:pk>/delete/',
         login_required(superuser_only(TeamDeleteView.as_view())), name="team_delete"),

    path('category/', login_required(superuser_only(CategoryListView.as_view())),
         name='category_list'),
    path('category/add/', login_required(superuser_only(CategoryCreateView.as_view())),
         name="category_add"),
    path('category/<int:pk>/', login_required(superuser_only(
        CategoryDetailView.as_view())), name="category_detail"),
    path('category/<int:pk>/change/',
         login_required(superuser_only(CategoryUpdateView.as_view())), name="category_change"),
    path('category/<int:pk>/delete/',
         login_required(superuser_only(CategoryDeleteView.as_view())), name="category_delete"),

    path('competition/', login_required(superuser_only(CompetitionListView.as_view())),
         name='competition_list'),
    path('competition/add/', login_required(superuser_only(
        CompetitionCreateView.as_view())), name="competition_add"),
    path('competition/<int:pk>/', login_required(superuser_only(
        CompetitionDetailView.as_view())), name="competition_detail"),
    path('competition/<int:pk>/change/', login_required(superuser_only(
        CompetitionUpdateView.as_view())), name="competition_change"),
    path('competition/<int:pk>/delete/', login_required(superuser_only(
        CompetitionDeleteView.as_view())), name="competition_delete"),

    path('referee/', login_required(superuser_only(RefereeListView.as_view())),
         name='referee_list'),
    path('referee/add/', login_required(superuser_only(RefereeCreateView.as_view())),
         name="referee_add"),
    path('referee/<int:pk>/',
         login_required(superuser_only(RefereeDetailView.as_view())), name="referee_detail"),
    path('referee/<int:pk>/change/',
         login_required(superuser_only(RefereeUpdateView.as_view())), name="referee_change"),
    path('referee/<int:pk>/delete/',
         login_required(superuser_only(RefereeDeleteView.as_view())), name="referee_delete"),

    path('match/', login_required(superuser_only(MatchListView.as_view())),
         name='match_list'),
    path('match/add/', login_required(superuser_only(MatchCreateView.as_view())),
         name="match_add"),
    path('match/<int:pk>/',
         login_required(superuser_only(MatchDetailView.as_view())), name="match_detail"),
    path('match/<int:pk>/change/',
         login_required(superuser_only(MatchUpdateView.as_view())), name="match_change"),
    path('match/<int:pk>/delete/',
         login_required(superuser_only(MatchDeleteView.as_view())), name="match_delete"),
]
