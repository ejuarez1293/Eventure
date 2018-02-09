import smtplib
from django.template import loader, RequestContext, Context
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.core import mail
from django.utils.html import strip_tags

#global variable for recipient list
recipientList =[]
emaiLinkDict = {}
items = []


def create_recipient_list(email, emailLink):
   recipientList.append(email)
   emaiLinkDict.update({email:emailLink})

def itemsPerEvent(item):
   items.append(item)

def sendEmailToAtendees(eventObject, newEmailInvitee , host, request):
    subject = 'Hey, You have been invited to' + eventObject.name
    #text_content = "This is the Text content"
    #html_message = loader.render_to_string('displayEvent.html', content)
    #print(text_content)
    #msg = EmailMultiAlternatives(subject, html_message, recipientList)
    #msg.content_subtype = "html"
    #smsg.send()

