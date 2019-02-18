from championship.models import Season, Match, Team, Category, Referee, Competition
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from view_breadcrumbs import ListBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin, CreateBreadcrumbMixin


#--------------------------- SEASON -------------------------------

class SeasonCreateView(CreateBreadcrumbMixin, CreateView):
    model = Season
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:season_list')


class SeasonListView(ListBreadcrumbMixin, ListView):
    model = Season
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('championship:season_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class SeasonUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Season
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:season_list')

    def get_object(self):
        return Season.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class SeasonDetailView(DetailBreadcrumbMixin, DetailView):
    model = Season

#--------------------------- TEAM -------------------------------

class TeamCreateView(CreateBreadcrumbMixin, CreateView):
    model = Team
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:team_list')


class TeamListView(ListBreadcrumbMixin, ListView):
    model = Team
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('championship:team_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class TeamUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Team
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:team_list')

    def get_object(self):
        return Team.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class TeamDetailView(DetailBreadcrumbMixin, DetailView):
    model = Team

#--------------------------- CATEGORY -------------------------------

class CategoryCreateView(CreateBreadcrumbMixin, CreateView):
    model = Category
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:category_list')


class CategoryListView(ListBreadcrumbMixin, ListView):
    model = Category
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('championship:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class CategoryUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:category_list')

    def get_object(self):
        return Category.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class CategoryDetailView(DetailBreadcrumbMixin, DetailView):
    model = Category

#--------------------------- COMPETITION -------------------------------

class CompetitionCreateView(CreateBreadcrumbMixin, CreateView):
    model = Competition
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:competition_list')


class CompetitionListView(ListBreadcrumbMixin, ListView):
    model = Competition
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('championship:competition_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class CompetitionUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Competition
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:competition_list')

    def get_object(self):
        return Competition.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class CompetitionDetailView(DetailBreadcrumbMixin, DetailView):
    model = Competition

#--------------------------- REFEREE -------------------------------

class RefereeCreateView(CreateBreadcrumbMixin, CreateView):
    model = Referee
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:referee_list')

class RefereeListView(ListBreadcrumbMixin, ListView):
    model = Referee
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('championship:referee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class RefereeUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Referee
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:referee_list')

    def get_object(self):
        return Referee.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class RefereeDetailView(DetailBreadcrumbMixin, DetailView):
    model = Referee

#--------------------------- MATCH -------------------------------

class MatchCreateView(CreateBreadcrumbMixin, CreateView):
    model = Match
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:match_list')

class MatchListView(ListBreadcrumbMixin, ListView):
    model = Match
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('championship:match_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class MatchUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Match
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:match_list')

    def get_object(self):
        return Match.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class MatchDetailView(DetailBreadcrumbMixin, DetailView):
    model = Match
