from assessment.views import QuestionListView, QuestionUpdateView, QuestionDetailView, QuestionCreateView, QuestionRListView, QuestionRUpdateView, QuestionRDetailView, QuestionRCreateView, AssessmentListView, AssessmentUpdateView, AssessmentDetailView, AssessmentCreateView, QuestionDeleteView, QuestionRDeleteView, AssessmentDeleteView
from django.urls import path


app_name = 'assessment'
urlpatterns = [
	path('question/', QuestionListView.as_view(), name='question_list'),
	path('question/add/', QuestionCreateView.as_view(), name="question_add"),
	path('question/<int:pk>/', QuestionDetailView.as_view(), name="question_detail"),
	path('question/<int:pk>/change/', QuestionUpdateView.as_view(), name="question_change"),
    path('question/<int:pk>/delete', QuestionDeleteView.as_view(), name="question_delete"),

	path('questionr/', QuestionRListView.as_view(), name='questionr_list'),
	path('questionr/add/', QuestionRCreateView.as_view(), name="questionr_add"),
	path('questionr/<int:pk>/', QuestionRDetailView.as_view(), name="questionr_detail"),
	path('questionr/<int:pk>/change/', QuestionRUpdateView.as_view(), name="questionr_change"),
    path('questionr/<int:pk>/delete', QuestionRDeleteView.as_view(), name="questionr_delete"),

	path('assessment/', AssessmentListView.as_view(), name='assessment_list'),
	path('assessment/add/', AssessmentCreateView.as_view(), name="assessment_add"),
	path('assessment/<int:pk>/', AssessmentDetailView.as_view(), name="assessment_detail"),
	path('assessment/<int:pk>/change/', AssessmentUpdateView.as_view(), name="assessment_change"),
	path('assessment/<int:pk>/delete', AssessmentDeleteView.as_view(), name="assessment_delete"),

]