from championship.models import Season, Match, Competition, Team, Category, Referee
from assessment.models import Assessment, Question, QuestionR
from customuser.models import CustomUser
from datetime import datetime
import random


def round_robin(units, sets = None):
    """ Generates a schedule of "fair" pairings from a list of units """
    count = len(units)
    sets = sets or (count - 1)
    half = int(count / 2)
    for turn in range(sets):
        left = units[:half]
        right = units[count - half - 1 + 1:][::-1]
        pairings = zip(left, right)
        if turn % 2 == 1:
            pairings = [(y, x) for (x, y) in pairings]
        units.insert(1, units.pop())
        yield pairings

s= Season(name="2018-2019")
s.save()

categories = ["SL", "SH2", "SH3", "SH4", "SD", "U21", "U17", "U15", "U13"]
for cat in categories:
	c = Category(name=cat)
	c.save()
c1 = Category.objects.get(name="SL")
comp = Competition(season=s,category=c1)
comp.save()
teams = ["RDM Mouscron", "CNT Tournai", "AZC Antwerpen", "RSCM Mechelen", "ENLWP La louvière", "MZV Eeklo", "RBP Poséidon"]
for team in teams:
    t = Team(name=team)
    t.save()
    comp.teams.add(t)

for i in range(1, 20):
    r = Referee(first_name="Ref%i" % i, last_name="FRBN")
    r.save()

dates = ['6/10/2018','13/10/2018','20/10/2018','27/10/2018','3/11/2018','10/11/2018','17/11/2018','24/11/2018','1/12/2018','8/12/2018','15/12/2018','19/01/2019','26/01/2019','2/02/2019','2/03/2019','9/03/2019']
for matches in list(round_robin(teams, sets = len(teams) * 2 - 2)):
    if type(matches) is list:
        ref_1 = random.sample(range(1, 20), 2*len(matches))
        ref_2 = random.sample(range(1, 20), 2*len(matches))
        for home,away in matches:
            teamH = Team.objects.get(name=home)
            teamA = Team.objects.get(name=away)
            m1 = Match(competition=comp,teamH=teamH,teamA=teamA,datetime=datetime.strptime("%s 20:00" % dates[0], "%d/%m/%Y %H:%M"))
            m1.save()
            m1.teams.add(teamH, teamA)
            m1.referees.add(Referee.objects.get(id=int(ref_1[0])),Referee.objects.get(id=int(ref_1[1])))
            del ref_1[0]
            del ref_1[0]
            m1.save()
            m2 = Match(competition=comp,teamH=teamA,teamA=teamH,datetime=datetime.strptime("%s 20:00" % dates[len(teams)], "%d/%m/%Y %H:%M"))
            m2.save()
            m2.teams.add(teamH, teamA)
            m2.referees.add(Referee.objects.get(id=int(ref_2[0])),Referee.objects.get(id=int(ref_2[1])))
            del ref_2[0]
            del ref_2[0]
            m2.save()
        del dates[0]

q1 = Question(name="Note globale de l'arbitre", priority=1)
q1.save()
q2 = Question(name="Impartialité", priority=2)
q2.save()
q3 = Question(name="Demande Supervision", priority=3, type_question='BOOL')
q3.save()


for m in Match.objects.all():
    for team in m.get_teams():
        for ref in m.get_referees():
            a = Assessment(match=m,team=team,referee=ref)
            a.save()
            for q in Question.objects.filter(active=True):
                qr = QuestionR.objects.create(question=q, priority=q.priority, answer=q.default_value)
                qr.save()
                a.questionnaire.add(qr)
            a.save()


u1 = CustomUser.objects.get(username="test")
u1.first_name = "Renaud"
u1.last_name = "Vilain"
u1.teams.add(Team.objects.get(name=teams[0]))
u1.categories.add(c1)
u1.save()

a = Assessment.objects.filter(match__datetime__lte=datetime.now())
for i in random.sample(range(0,len(a)),20+random.randint(0, len(a)-20)):
    a[i].confirm = True
    a[i].datetime_confirm = datetime.now()
    a[i].user = u1
    for qr in a[i].get_sorted_questions():
        qr.answer = random.randint(qr.question.min_value, qr.question.max_value)
        qr.save()
    a[i].save()
