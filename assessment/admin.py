from django.contrib import admin
from assessment.models import Question, QuestionR, Assessment

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    pass

class QuestionRAdmin(admin.ModelAdmin):
    pass

class AssessmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionR, QuestionRAdmin)
admin.site.register(Assessment, AssessmentAdmin)