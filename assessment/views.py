from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import user_can_access
from championship.models import Match, Referee
from .models import Evaluation, Question, QuestionR

# Create your views here.
@login_required
def stats(request):
    c = {}
    refs=[]
    q = Question.objects.all().order_by('id')
    c['questions'] = Question.objects.all().order_by('id')
    for r in Referee.objects.all():
        d = {}
        d['name'] = r.get_full_name()
        eval_r = Evaluation.objects.filter(referee=r, confirm=True)
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
        e = Evaluation.objects.get(id=eid)
        e.confirm = True
        e.user = request.user
        e.datetime_confirm = datetime.now()
        e.save()
    c['match'] = Match.objects.get(id=match_id)
    c['evaluations'] = Evaluation.objects.filter(match=c['match'])
    c['nb_ref'] = len(c['evaluations'])
    return render(request, 'evaluation.html', c)