from assessment.views import QuestionListView, QuestionUpdateView, QuestionDetailView, QuestionCreateView, QuestionDeleteView, QuestionRListView, QuestionRUpdateView, QuestionRDetailView, QuestionRCreateView, QuestionRDeleteView, AssessmentRefereeListView, AssessmentRefereeUpdateView, AssessmentRefereeDetailView, AssessmentRefereeCreateView, AssessmentRefereeDeleteView, AssessmentMatchListView, AssessmentMatchUpdateView, AssessmentMatchDetailView, AssessmentMatchCreateView, AssessmentMatchDeleteView

from customuser.decorators import superuser_only
from django.contrib.auth.decorators import login_required
from django.urls import path


app_name = 'assessment'
urlpatterns = [
	path('question/', login_required(superuser_only(QuestionListView.as_view())), name='question_list'),
	path('question/add/', login_required(superuser_only(QuestionCreateView.as_view())), name="question_add"),
	path('question/<int:pk>/', login_required(superuser_only(QuestionDetailView.as_view())), name="question_detail"),
	path('question/<int:pk>/change/', login_required(superuser_only(QuestionUpdateView.as_view())), name="question_change"),
    path('question/<int:pk>/delete/', login_required(superuser_only(QuestionDeleteView.as_view())), name="question_delete"),

	path('questionr/', login_required(superuser_only(QuestionRListView.as_view())), name='questionr_list'),
	path('questionr/add/', login_required(superuser_only(QuestionRCreateView.as_view())), name="questionr_add"),
	path('questionr/<int:pk>/', login_required(superuser_only(QuestionRDetailView.as_view())), name="questionr_detail"),
	path('questionr/<int:pk>/change/', login_required(superuser_only(QuestionRUpdateView.as_view())), name="questionr_change"),
    path('questionr/<int:pk>/delete/', login_required(superuser_only(QuestionRDeleteView.as_view())), name="questionr_delete"),

	path('assessment_referee/', login_required(superuser_only(AssessmentRefereeListView.as_view())), name='assessment_referee_list'),
	path('assessment_referee/add/', login_required(superuser_only(AssessmentRefereeCreateView.as_view())), name="assessment_referee_add"),
	path('assessment_referee/<int:pk>/', login_required(superuser_only(AssessmentRefereeDetailView.as_view())), name="assessment_referee_detail"),
	path('assessment_referee/<int:pk>/change/', login_required(superuser_only(AssessmentRefereeUpdateView.as_view())), name="assessment_referee_change"),
	path('assessment_referee/<int:pk>/delete/', login_required(superuser_only(AssessmentRefereeDeleteView.as_view())), name="assessment_referee_delete"),

	path('assessment_match/', login_required(superuser_only(AssessmentMatchListView.as_view())), name='assessment_match_list'),
	path('assessment_match/add/', login_required(superuser_only(AssessmentMatchCreateView.as_view())), name="assessment_match_add"),
	path('assessment_match/<int:pk>/', login_required(superuser_only(AssessmentMatchDetailView.as_view())), name="assessment_match_detail"),
	path('assessment_match/<int:pk>/change/', login_required(superuser_only(AssessmentMatchUpdateView.as_view())), name="assessment_match_change"),
	path('assessment_match/<int:pk>/delete/', login_required(superuser_only(AssessmentMatchDeleteView.as_view())), name="assessment_match_delete"),

]