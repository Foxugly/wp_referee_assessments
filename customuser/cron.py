from customuser.models import CustomUser
from assessment.models AssessmentMatch


def send_mail():
  ams = AssessmentMatch.objects.filter(sent=False)
  # il faut checker la date
  for am in ams:
    usersHome = CustomUser.objects.filter(teams__in=am.match.teamH, categories__in=am.match.competition.category)
    for uh is usersHome:
      print(uh)
      #send mail
    usersAway = CustomUser.objects.filter(teams__in=am.match.teamA, categories__in=am.match.competition.category)
    for ua is usersAway:
      print(ua)
      #send mail
    am.sent = True
    am.save()
