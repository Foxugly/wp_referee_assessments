from customuser.models import CustomUser
from assessment.models AssessmentMatch
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context



def send_mail(customuser)
  plaintext = get_template('mail/email_%s.txt' % customuser.language)
  htmly = get_template('mail/email_%s.html' % customuser.language)
  d = Context({ 'user': customuser, 'match':match})
  subject, from_email, to = '[FRBN-KBZB] Referees assessment', 'wp_assessment@belswim.be', customuser.email
  text_content = plaintext.render(d)
  html_content = htmly.render(d)
  msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
  msg.attach_alternative(html_content, "text/html")
  #msg.send()


def send_mail():
  end = timezone.date()
  start = end - timezone.timedelta(days=7)
  ams = AssessmentMatch.objects.filter(sent=False, match__datetime__range=[start, end])
  # il faut checker la date
  for am in ams:
    print(am)
    usersHome = CustomUser.objects.filter(teams__in=am.match.teamH, categories__in=am.match.competition.category)
    for uh in usersHome:
      print(uh)
      send_mail(uh)
      #send mail
    usersAway = CustomUser.objects.filter(teams__in=am.match.teamA, categories__in=am.match.competition.category)
    for ua in usersAway:
      print(ua)
      send_mail(uh)
      #send mail
    am.sent = True
    am.save()
