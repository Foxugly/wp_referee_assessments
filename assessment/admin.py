from django.contrib import admin
from assessment.models import Question, QuestionR, AssessmentReferee, AssessmentMatch

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    pass


class QuestionRAdmin(admin.ModelAdmin):
    pass


class AssessmentRefereeAdmin(admin.ModelAdmin):
    pass


class AssessmentMatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionR, QuestionRAdmin)
admin.site.register(AssessmentMatch, AssessmentMatchAdmin)
admin.site.register(AssessmentReferee, AssessmentRefereeAdmin)
