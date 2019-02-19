from view_breadcrumbs import ListBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin, CreateBreadcrumbMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from assessment.models import Question, QuestionR, Assessment
from django.urls import reverse_lazy
# Create your views here.
#--------------------------- SEASON -------------------------------

class QuestionCreateView(CreateBreadcrumbMixin, CreateView):
    model = Question
    fields = ['name', 'priority', 'active', 'type_question', 'min_value', 'max_value', 'default_value']
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:question_list')


class QuestionListView(ListBreadcrumbMixin, ListView):
    model = Question
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('assessment:question_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class QuestionUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Question
    fields = ['name', 'priority', 'active', 'type_question', 'min_value', 'max_value', 'default_value']
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:question_list')

    def get_object(self):
        return Question.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class QuestionDetailView(DetailBreadcrumbMixin, DetailView):
    model = Question

#--------------------------- QUESTIONR -------------------------------

class QuestionRCreateView(CreateBreadcrumbMixin, CreateView):
    model = QuestionR
    fields = ['question', 'priority', 'active', 'answer']
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:questionr_list')


class QuestionRListView(ListBreadcrumbMixin, ListView):
    model = QuestionR
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('assessment:questionr_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class QuestionRUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = QuestionR
    fields = ['question', 'priority', 'active', 'answer']
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:questionr_list')

    def get_object(self):
        return QuestionR.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class QuestionRDetailView(DetailBreadcrumbMixin, DetailView):
    model = QuestionR

#--------------------------- ASSESSMENT -------------------------------

class AssessmentCreateView(CreateBreadcrumbMixin, CreateView):
    model = Assessment
    fields = ['match', 'referee', 'user', 'team', 'questionnaire', 'confirm', 'datetime_confirm']
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:assessment_list')


class AssessmentListView(ListBreadcrumbMixin, ListView):
    model = Assessment
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('assessment:assessment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class AssessmentUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Assessment
    fields = ['match', 'referee', 'user', 'team', 'questionnaire', 'confirm', 'datetime_confirm']
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:assessment_list')

    def get_object(self):
        return Assessment.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class AssessmentDetailView(DetailBreadcrumbMixin, DetailView):
    model = Assessment



