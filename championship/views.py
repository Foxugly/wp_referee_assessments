from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Match, Team, Category, Referee
from assessment.models import Evaluation, Question, QuestionR
from users.models import MyUser
from datetime import datetime
from django.shortcuts import redirect


# Create your views here.
@login_required
def home(request):
    c = {}
    now = datetime.now()
    c['now'] = now
    teams = request.user.get_teams()
    categories = request.user.get_categories()
    c['teams'] = list(teams)
    c['categories'] = list(categories)
    m_eval_to_created = Match.objects.filter(teams__in=teams,category__in=categories,datetime__lte=now)
    for m_eval in m_eval_to_created:
        for team in teams:
            if team in m_eval.get_teams():
                for r in m_eval.get_referees():
                    if not Evaluation.objects.filter(match=m_eval,team=team,referee=r):
                        e = Evaluation(match=m_eval,team=team,user=request.user,referee=r)
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
def init(request):
    t1 = Team(name="Ixelles")
    t1.save()  
    t2 = Team(name="Ciney")
    t2.save()
    t3 = Team(name="Tournai")
    t3.save()
    t4 = Team(name="Mouscron")
    t4.save()
    r1 = Referee(first_name="Alice", last_name="FRBN")
    r1.save()
    r2 = Referee(first_name="Bob", last_name="FRBN")
    r2.save()
    r3 = Referee(first_name="Eve", last_name="FRBN")
    r3.save()
    c1 = Category(name="SL")
    c1.save()
    c1.teams.add(t3)
    c1.teams.add(t4)
    c1.save()
    c2 = Category(name="SH4")
    c2.save()
    c2.teams.add(t1)
    c2.teams.add(t2)
    c2.save()
    m1 = Match(category=c1,teamH=t4,teamA=t3,datetime=datetime.strptime("1/12/18 20:00", "%d/%m/%y %H:%M"))
    m1.save()
    m1.referees.add(r1)
    m1.referees.add(r2)
    m1.teams.add(t3)
    m1.teams.add(t4)
    m1.save()
    m2 = Match(category=c1,teamH=t3,teamA=t4,datetime=datetime.strptime("1/3/19 20:00", "%d/%m/%y %H:%M"))
    m2.save()
    m2.referees.add(r1)
    m2.referees.add(r3)
    m2.teams.add(t3)
    m2.teams.add(t4)
    m2.save()
    m3 = Match(category=c2,teamH=t1,teamA=t2,datetime=datetime.strptime("1/12/18 20:00", "%d/%m/%y %H:%M"))
    m3.save()
    m3.referees.add(r2)
    m3.teams.add(t1)
    m3.teams.add(t2)
    m3.save()
    m4 = Match(category=c2,teamH=t2,teamA=t1,datetime=datetime.strptime("1/3/19 20:00", "%d/%m/%y %H:%M"))
    m4.save()
    m4.referees.add(r3)
    m4.teams.add(t1)
    m4.teams.add(t2)
    m4.save()
    q1 = Question(name="Note globale de l'arbitre", priority=1)
    q1.save()
    q2 = Question(name="Impartialité", priority=2)
    q2.save()
    q3 = Question(name="Demande Supervision", priority=3, type_question='BOOL')
    q3.save()
    u2 = MyUser(username="test2", email='test2@test2.be', first_name='test2', last_name='test2')
    u2.set_password("test2test2")
    u2.save()
    u2.teams.add(t4)
    u2.categories.add(c1)
    u2.save()
    request.user.teams.add(t1)
    request.user.categories.add(c2)
    request.user.save()
    return redirect('/')