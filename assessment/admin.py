from django.contrib import admin
from .models import Question, QuestionR, Evaluation

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    pass

class QuestionRAdmin(admin.ModelAdmin):
    pass

class EvaluationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionR, QuestionRAdmin)
admin.site.register(Evaluation, EvaluationAdmin)