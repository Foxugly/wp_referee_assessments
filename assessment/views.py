from view_breadcrumbs import ListBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin, CreateBreadcrumbMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from assessment.models import Question, QuestionR, AssessmentReferee, AssessmentMatch
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
# --------------------------- SEASON -------------------------------


class QuestionCreateView(CreateBreadcrumbMixin, CreateView):
    model = Question
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:question_list')
    success_message = _('object created.')


class QuestionListView(ListBreadcrumbMixin, ListView):
    model = Question
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    #success_url = reverse_lazy('assessment:question_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class QuestionUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Question
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:question_list')
    success_message = _('object updated.')

    def get_object(self):
        return Question.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class QuestionDetailView(DetailBreadcrumbMixin, DetailView):
    model = Question
    template_name = 'detail.html'


class QuestionDeleteView(SuccessMessageMixin, DeleteView):
    model = Question
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('assessment:question_list')

# --------------------------- QUESTIONR -------------------------------


class QuestionRCreateView(CreateBreadcrumbMixin, CreateView):
    model = QuestionR
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:questionr_list')
    success_message = _('object created.')


class QuestionRListView(ListBreadcrumbMixin, ListView):
    model = QuestionR
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    #success_url = reverse_lazy('assessment:questionr_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class QuestionRUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = QuestionR
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:questionr_list')
    success_message = _('object updated.')

    def get_object(self):
        return QuestionR.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class QuestionRDetailView(DetailBreadcrumbMixin, DetailView):
    model = QuestionR
    template_name = 'detail.html'


class QuestionRDeleteView(SuccessMessageMixin, DeleteView):
    model = QuestionR
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('assessment:questionr_list')

# --------------------------- ASSESSMENT MATCH---------------------------


class AssessmentMatchCreateView(CreateBreadcrumbMixin, CreateView):
    model = AssessmentMatch
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:assessmentmatch_list')
    success_message = _('object created.')


class AssessmentMatchListView(ListBreadcrumbMixin, ListView):
    model = AssessmentMatch
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class AssessmentMatchUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = AssessmentMatch
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:assessmentmatch_list')
    success_message = _('object updated.')

    def get_object(self):
        return AssessmentMatch.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class AssessmentMatchDetailView(DetailBreadcrumbMixin, DetailView):
    model = AssessmentMatch
    template_name = 'detail.html'


class AssessmentMatchDeleteView(SuccessMessageMixin, DeleteView):
    model = AssessmentMatch
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('assessment:assessmentmatch_list')

# --------------------------- ASSESSMENT REFEREE--------------------------


class AssessmentRefereeCreateView(CreateBreadcrumbMixin, CreateView):
    model = AssessmentReferee
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:assessmentreferee_list')
    success_message = _('object created.')


class AssessmentRefereeListView(ListBreadcrumbMixin, ListView):
    model = AssessmentReferee
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class AssessmentRefereeUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = AssessmentReferee
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:assessmentreferee_list')
    success_message = _('object updated.')

    def get_object(self):
        return AssessmentReferee.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class AssessmentRefereeDetailView(DetailBreadcrumbMixin, DetailView):
    model = AssessmentReferee
    template_name = 'detail.html'


class AssessmentRefereeDeleteView(SuccessMessageMixin, DeleteView):
    model = AssessmentReferee
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('assessment:assessmentreferee_list')
