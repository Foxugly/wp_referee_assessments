from championship.models import Season, Match, Team, Category, Referee, Competition
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from view_breadcrumbs import ListBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin, CreateBreadcrumbMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


# --------------------------- SEASON -------------------------------


class SeasonCreateView(CreateBreadcrumbMixin, CreateView):
    model = Season
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:season_list')
    success_message = _('object created.')


class SeasonListView(ListBreadcrumbMixin, ListView):
    model = Season
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    #success_url = reverse_lazy('championship:season_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class SeasonUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Season
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:season_list')
    success_message = _('object updated.')

    def get_object(self):
        return Season.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class SeasonDetailView(DetailBreadcrumbMixin, DetailView):
    model = Season
    template_name = 'detail.html'


class SeasonDeleteView(SuccessMessageMixin, DeleteView):
    model = Season
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('championship:season_list')

# --------------------------- TEAM -------------------------------


class TeamCreateView(CreateBreadcrumbMixin, CreateView):
    model = Team
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:team_list')
    success_message = _('object created.')


class TeamListView(ListBreadcrumbMixin, ListView):
    model = Team
    paginate_by = 10
    ordering = ['pk']
    template_name = 'list.html'
    #success_url = reverse_lazy('championship:team_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class TeamUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Team
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:team_list')
    success_message = _('object updated.')

    def get_object(self):
        return Team.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class TeamDetailView(DetailBreadcrumbMixin, DetailView):
    model = Team
    template_name = 'detail.html'


class TeamDeleteView(SuccessMessageMixin, DeleteView):
    model = Team
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('championship:team_list')

# --------------------------- CATEGORY -------------------------------


class CategoryCreateView(CreateBreadcrumbMixin, CreateView):
    model = Category
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:category_list')
    success_message = _('object created.')


class CategoryListView(ListBreadcrumbMixin, ListView):
    model = Category
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    #success_url = reverse_lazy('championship:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class CategoryUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:category_list')
    success_message = _('object updated.')

    def get_object(self):
        return Category.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class CategoryDetailView(DetailBreadcrumbMixin, DetailView):
    model = Category
    template_name = 'detail.html'


class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    model = Category
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('championship:category_list')

# --------------------------- COMPETITION -------------------------------


class CompetitionCreateView(CreateBreadcrumbMixin, CreateView):
    model = Competition
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:competition_list')
    success_message = _('object created.')


class CompetitionListView(ListBreadcrumbMixin, ListView):
    model = Competition
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    #success_url = reverse_lazy('championship:competition_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class CompetitionUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Competition
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:competition_list')
    success_message = _('object updated.')

    def get_object(self):
        return Competition.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class CompetitionDetailView(DetailBreadcrumbMixin, DetailView):
    model = Competition
    template_name = 'detail.html'


class CompetitionDeleteView(SuccessMessageMixin, DeleteView):
    model = Competition
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('championship:competition_list')

# --------------------------- REFEREE -------------------------------


class RefereeCreateView(CreateBreadcrumbMixin, CreateView):
    model = Referee
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:referee_list')
    success_message = _('object created.')


class RefereeListView(ListBreadcrumbMixin, ListView):
    model = Referee
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    #success_url = reverse_lazy('championship:referee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class RefereeUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Referee
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:referee_list')
    success_message = _('object updated.')

    def get_object(self):
        return Referee.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class RefereeDetailView(DetailBreadcrumbMixin, DetailView):
    model = Referee
    template_name = 'detail.html'


class RefereeDeleteView(SuccessMessageMixin, DeleteView):
    model = Referee
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('championship:referee_list')

# --------------------------- MATCH -------------------------------


class MatchCreateView(CreateBreadcrumbMixin, CreateView):
    model = Match
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:match_list')
    success_message = _('object created.')

    def get_context_data(self, **kwargs):
        context = super(MatchCreateView, self).get_context_data(**kwargs)
        context['add_class_to_fields'] = {'id_datetime': 'datetime'}
        return context


class MatchListView(ListBreadcrumbMixin, ListView):
    model = Match
    # paginate_by = 10
    ordering = ['pk']
    template_name = 'list_datatable.html'
    #success_url = reverse_lazy('championship:match_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class MatchUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Match
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('championship:match_list')
    success_message = _('object updated.')

    def get_object(self):
        return Match.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class MatchDetailView(DetailBreadcrumbMixin, DetailView):
    model = Match
    template_name = 'detail.html'


class MatchDeleteView(SuccessMessageMixin, DeleteView):
    model = Match
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('championship:match_list')
