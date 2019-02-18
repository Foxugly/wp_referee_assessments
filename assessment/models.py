from django.db import models
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _
from championship.models import Match, Referee, Team, Category


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


class Assessment(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name=_('match'))
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE, verbose_name=_('referee'))
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('user'))
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_('team'))
    questionnaire = models.ManyToManyField(QuestionR, blank=True, verbose_name=_('type of question'))
    confirm = models.BooleanField(_('confirmation'), default=False)
    datetime_confirm = models.DateTimeField(_('datetime of confirmation'), blank=True, null=True)

    def get_sorted_questions(self):
        return self.questionnaire.all().order_by('priority')

    def __str__(self):
        return "%s - %s " % (self.match, self.referee)