"""Customuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, reverse
from customuser.views import CustomUserUpdateView 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import translation
from django import http
import json
from customuser.decorators import check_lang, user_can_access, referee_admin_required
from championship.models import Match, Referee
from assessment.models import Assessment, Question, QuestionR
from datetime import datetime
from django.conf.urls.static import static


#TODO home, evaluation, stats

def set_language(request):
    if 'lang' in request.GET and 'next' in request.GET:
        if translation.LANGUAGE_SESSION_KEY in request.session:
            del request.session[translation.LANGUAGE_SESSION_KEY]
        translation.activate(request.GET.get('lang'))
        request.session[translation.LANGUAGE_SESSION_KEY] = request.GET.get('lang')
        return HttpResponseRedirect(request.GET.get('next'))
    else:
        return reverse('home')


@login_required
def home(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    c = {}
    now = datetime.now()
    c['now'] = now
    teams = request.user.get_teams()
    categories = request.user.get_categories()
    c['teams'] = list(teams)
    c['categories'] = list(categories)
    if len(teams) and len(categories):
        m_eval_to_created = Match.objects.filter(teams__in=teams,category__in=categories,datetime__lte=now)
        for m_eval in m_eval_to_created:
            for team in teams:
                if team in m_eval.get_teams():
                    for r in m_eval.get_referees():
                        if not Assessment.objects.filter(match=m_eval,team=team,referee=r):
                            e = Assessment(match=m_eval,team=team,user=request.user,referee=r)
                            e.save()
                            for q in Question.objects.all():
                                qr = QuestionR.objects.create(question=q, priority=q.priority, answer=q.default_value)
                                qr.save()
                                e.questionnaire.add(qr)
                            e.save()
        c['all'] = Match.objects.filter(teams__in=teams, category__in=categories).order_by("datetime")
        c['n_all'] = len(c['all'])
        c['done'] = []
        c['todo'] = []
        for m in Match.objects.filter(teams__in=teams, category__in=categories,datetime__lte=now).order_by("datetime"):
            done = True
            exist = False
            for e in Evaluation.objects.filter(match=m):
                exist = True
                done = done and e.confirm
            if exist:
                if done:
                    c['done'].append(m)
                else:
                    c['todo'].append(m)
            else:
                c['todo'].append(m)
        
        c['n_done'] = len(c['done'])
        c['n_todo'] = len(c['todo'])

        c['next'] = Match.objects.filter(teams__in=teams,category__in=categories,datetime__gte=now).order_by("datetime")
        c['n_next'] = len(c['next'])
    return render(request, 'club.html', c)


@login_required
@referee_admin_required
def stats(request):
    c = {}
    refs=[]
    q = Question.objects.all().order_by('id')
    c['questions'] = Question.objects.all().order_by('id')
    for r in Referee.objects.all():
        d = {}
        d['name'] = r.get_full_name()
        eval_r = Assessment.objects.filter(referee=r, confirm=True)
        d['matches'] = len(eval_r)
        notes = []
        values = {}
        n = 0
        for e in eval_r:
            n+=1
            for qr in e.get_sorted_questions():
                if qr.question.id not in values :
                    values[qr.question.id] = qr.answer
                else:
                    values[qr.question.id] += qr.answer
        for q in c['questions']:
            notes.append(0 if not n else int((values[q.id]/n)*10))
            d['notes'] = notes
        refs.append(d)
    c['refs'] = refs
    return render(request, 'stats.html', c)

@login_required
@user_can_access
def evaluation(request, match_id):
    c = {}
    c['id']= match_id
    if request.method == 'POST':
        d = dict(request.POST)
        for key in d.keys():
            if "question" in key :
                q_id = key.split("question_")[1]
                qr = QuestionR.objects.get(id=q_id)
                answer = int(d[key][0]) if type(d[key]) == list else  int(d[key])
                qr.answer = answer
                qr.save()
        eid = int(d['eval_id'][0])
        e = Assessment.objects.get(id=eid)
        e.confirm = True
        e.user = request.user
        e.datetime_confirm = datetime.now()
        e.save()
    c['match'] = Match.objects.get(id=match_id)
    c['evaluations'] = Assessment.objects.filter(match=c['match'])
    c['nb_ref'] = len(c['evaluations'])
    return render(request, 'evaluation.html', c)

urlpatterns = [
    path('',login_required(home), name='home'),
    path('lang/', set_language, name='lang'),
    path('evaluation/<int:match_id>/',login_required(evaluation), name="evaluation"),
    path('stats/',login_required(stats), name="stats"),
    path('admin/', admin.site.urls),
    path('championship/', include('championship.urls', namespace='championship')),
    path('assessment/', include('assessment.urls', namespace='assessment')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/update/', check_lang(CustomUserUpdateView.as_view()), name='update_user'),
    path('hijack/', include('hijack.urls', namespace='hijack')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [ path('__debug__/', include(debug_toolbar.urls)), ]
