from view_breadcrumbs import ListBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin, CreateBreadcrumbMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from assessment.models import Question, QuestionR, Assessment
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
#--------------------------- SEASON -------------------------------

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
        context['model']= self.model
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
        context['model']= self.model
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

#--------------------------- QUESTIONR -------------------------------

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
        context['model']= self.model
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
        context['model']= self.model
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

#--------------------------- ASSESSMENT -------------------------------

class AssessmentCreateView(CreateBreadcrumbMixin, CreateView):
    model = Assessment
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:assessment_list')
    success_message = _('object created.')


class AssessmentListView(ListBreadcrumbMixin, ListView):
    model = Assessment
    paginate_by = 20
    ordering = ['pk']
    template_name = 'list.html'
    #success_url = reverse_lazy('assessment:assessment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class AssessmentUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Assessment
    fields = "__all__"
    template_name = 'update.html'
    success_url = reverse_lazy('assessment:assessment_list')
    success_message = _('object updated.')

    def get_object(self):
        return Assessment.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model']= self.model
        return context


class AssessmentDetailView(DetailBreadcrumbMixin, DetailView):
    model = Assessment
    template_name = 'detail.html'


class AssessmentDeleteView(SuccessMessageMixin, DeleteView):
    model = Assessment
    success_message = _('object deleted.')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('assessment:assessment_list')



