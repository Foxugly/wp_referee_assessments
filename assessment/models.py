from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from championship.models import Match, Referee, Team, Category
from customuser.models import CustomUser


# Create your models here.
class Question(models.Model):
    TYPE_QUESTION_CHOICES = (
    ('INT', _("integer")),
    ('BOOL', _("boolean")),
    )
    name = models.CharField(_("question"), max_length=100)
    priority = models.IntegerField(_("priority"))
    active = models.BooleanField(_('active'), default=True)
    type_question = models.CharField(
        max_length=5,
        choices=TYPE_QUESTION_CHOICES,
        default='INT', verbose_name=_('type of question')
    )
    min_value = models.IntegerField(_('minimum value'), default = 0)
    max_value = models.IntegerField(_('maximum value'), default = 10)
    default_value = models.IntegerField(_('default value'), default = 5)

    def __str__(self):
        return self.name.strip()
    
    def save(self, *args, **kwargs):
        if self.type_question == 'BOOL':
            self.min_value = 0
            self.max_value = 1
            if self.default_value not in (0, 1):
                self.default_value = 0
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('assessment:question_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('assessment:question_add')

    def get_detail_url(self):
        return reverse('assessment:question_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('assessment:question_delete', kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('assessment:question_list')

    class Meta:
        verbose_name = _('Question')


class QuestionR(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_('question'))
    priority = models.IntegerField(_('priority'))
    active = models.BooleanField(_('active'), default=True)
    answer = models.IntegerField(_('answer'), default=0)

    def __str__(self):
        return "%s %s" % (self.id, self.question)

    def clean(self):
        if self.question.type_question in ('INT', 'BOOL'):
            if not self.question.min_value <= int(self.answer) <= self.question.max_value+1:
                raise ValidationError(_('Answer is not in the limited range.'))

    def get_absolute_url(self):
        return reverse('assessment:questionr_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('assessment:questionr_add')

    def get_detail_url(self):
        return reverse('assessment:questionr_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('assessment:questionr_delete', kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('assessment:questionr_list')

    class Meta:
        verbose_name = _('QuestionR')


class AssessmentReferee(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name=_('match'))
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE, verbose_name=_('referee'))
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('user'), null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_('team'))
    questionnaire = models.ManyToManyField(QuestionR, blank=True, verbose_name=_('questionnaire'))
    confirm = models.BooleanField(_('confirmation'), default=False)
    datetime_confirm = models.DateTimeField(_('datetime of confirmation'), blank=True, null=True)
    refer_am = models.ForeignKey('assessment.AssessmentMatch', verbose_name=_('Assessment  Match'), related_name="back_am", null=True,
                                   on_delete=models.CASCADE)

    def create_questionrs(self):
        for q in Question.objects.filter(active=True):
            qr = QuestionR.objects.create(question=q, priority=q.priority, answer=q.default_value)
            qr.save()
            self.questionnaire.add(qr)

    def get_sorted_questions(self):
        return self.questionnaire.all().order_by('priority')

    def __str__(self):
        return "%s - %s " % (self.match, self.referee)

    def get_absolute_url(self):
        return reverse('assessment:assessmentreferee_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('assessment:assessmentreferee_add')

    def get_detail_url(self):
        return reverse('assessment:assessmentreferee_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('assessment:assessmentreferee_delete', kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('assessment:assessmentreferee_list')

    class Meta:
        verbose_name = _('Assessment Referee')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.refer_am.check_done()


class AssessmentMatch(models.Model):
    done = models.BooleanField(_('Done'), default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_('team'))
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name=_('match'))
    assessment_referees = models.ManyToManyField(AssessmentReferee, blank=True, verbose_name=_('Assessment referees'))

    def __str__(self):
        return "%s -------- %s " % (self.match, self.team)

    def get_absolute_url(self):
        return reverse('assessment:assessmentmatch_change', kwargs={'pk': self.pk})

    def get_add_url(self):
        return  reverse('assessment:assessmentmatch_add')

    def get_detail_url(self):
        return reverse('assessment:assessmentmatch_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('assessment:assessmentmatch_delete', kwargs={'pk': self.pkS})

    def get_list_url(self):
        return reverse('assessment:assessmentmatch_list')

    def create_assessments_referee(self):
        for r in self.match.get_referees():
            ar = AssessmentReferee(match=self.match,referee=r,team=self.team,refer_am=self)
            ar.save()
            ar.create_questionrs()
            self.assessment_referees.add(ar)

    def check_done(self):
        done = True
        for ar in self.assessment_referees.all():
            done = done and ar.confirm
        self.done = done
        self.save()

    class Meta:
        verbose_name = _('Assessment Match')
