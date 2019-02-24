
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import translation, timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from assessment.models import AssessmentReferee, AssessmentMatch, Question, QuestionR
from customuser.models import CustomUser
from customuser.forms import CustomUserForm
from customuser.decorators import check_lang, user_can_access, referee_admin_required
from championship.models import Season, Competition, Match, Referee


class CustomUserUpdateView(SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'update.html'
    success_url = reverse_lazy('update_user')
    success_message = _('Changes saved.')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


@login_required
def home(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    c = {}
    now = timezone.now()
    c['now'] = now
    teams = request.user.get_teams()
    categories = request.user.get_categories()
    season = Season.objects.get(active=True)
    comp = Competition.objects.filter(season=season, category__in=categories)
    c['teams'] = list(teams)
    c['categories'] = list(categories)
    if len(teams) and len(categories):
        c['all'] = AssessmentMatch.objects.filter(
            team__in=teams, match__competition__in=comp).order_by("match__datetime")
        c['n_all'] = len(c['all'])
        c['done'] = []
        c['todo'] = []
        for am in AssessmentMatch.objects.filter(team__in=teams, match__competition__in=comp, match__datetime__lte=now).order_by("match__datetime"):
            if am.done:
                c['done'].append(am)
            else:
                c['todo'].append(am)
        c['n_done'] = len(c['done'])
        c['n_todo'] = len(c['todo'])
        c['next'] = AssessmentMatch.objects.filter(
            team__in=teams, match__competition__in=comp, match__datetime__gte=now).order_by("match__datetime")
        c['n_next'] = len(c['next'])
    return render(request, 'club.html', c)


@login_required
@referee_admin_required
def stats(request):
    c = {}
    refs = []
    q = Question.objects.all().order_by('id')
    c['questions'] = Question.objects.all().order_by('id')
    for r in Referee.objects.all():
        d = {}
        d['name'] = r.get_full_name()
        eval_r = AssessmentReferee.objects.filter(referee=r, confirm=True)
        d['matches'] = len(eval_r)
        notes = []
        values = {}
        n = 0
        for e in eval_r:
            n += 1
            for qr in e.get_sorted_questions():
                if qr.question.id not in values:
                    values[qr.question.id] = qr.answer/qr.question.max_value
                else:
                    values[qr.question.id] += qr.answer/qr.question.max_value
        for q in c['questions']:
            notes.append(0 if not n else int((values[q.id]/n)*100))
            d['notes'] = notes
        refs.append(d)
    c['refs'] = refs
    return render(request, 'stats.html', c)


@login_required
@user_can_access
def evaluation(request, am_id):
    c = {}
    c['id'] = am_id
    am = AssessmentMatch.objects.get(id=am_id)
    if request.method == 'POST':
        d = dict(request.POST)
        for key in d.keys():
            if "question" in key:
                q_id = key.split("question_")[1]
                qr = QuestionR.objects.get(id=q_id)
                answer = int(d[key][0]) if type(
                    d[key]) == list else int(d[key])
                qr.answer = answer
                qr.save()
        eid = int(d['eval_id'][0])
        e = AssessmentReferee.objects.get(
            id=eid, team__in=request.user.get_teams())
        e.confirm = True
        e.user = request.user
        e.datetime_confirm = timezone.now()
        e.save()
        am = AssessmentMatch.objects.get(id=am_id)
        am.check_done()

    c['am'] = am
    c['nb_ref'] = len(am.assessment_referees.all())
    return render(request, 'evaluation.html', c)
