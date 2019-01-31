
from django.template import loader, RequestContext, Context
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.core import mail
from django.conf import settings
from main_app import models, views
from django.utils.html import strip_tags
##import html2text

#global variable for recipient list
global recipientList, emaiLinkDict, items
recipientList =[]
emaiLinkDict = {}
items = []

def resetGlobals():
    global recipientList,emaiLinkDict,items
    recipientList = []
    emaiLinkDict = {}
    items = []

def create_recipient_list(email, emailLink):
   recipientList.append(email)
   emaiLinkDict.update({email:emailLink})

def sendEmailToAtendees(eventObject):
    connection = mail.get_connection()
    connection.open()
    subject = "You Have been invited to: " + eventObject.name
    for attendeeEmail in recipientList:
        message = 'Hey, ' + attendeeEmail + ' you have been invited to: ' + eventObject.name + '\nClick on the link to set your RSVP status:\n' + emaiLinkDict.get(attendeeEmail)
        email = EmailMessage(subject,message, settings.DEFAULT_FROM_EMAIL,[attendeeEmail],connection=connection)
        email.send()
    resetGlobals()
    connection.close()

def sendEventChangeNotification(newEvent):
    connection = mail.get_connection()
    connection.open()
    attendees = models.Attendee.objects.filter(eventID=newEvent.id)
    subject = "Event: " + newEvent.name + " has been modified"
    for attendee in attendees:
        attendeeEmail = attendee.email
        emaiLink = views.createInviteLink(newEvent,attendee)
        create_recipient_list(attendee.email,emaiLink)
        message = 'Hey, ' + attendeeEmail + ' the event you have been invited to: ' + newEvent.name + ' has been modified\nClick on the link to see the changes:\n' + emaiLinkDict.get(
            attendeeEmail)
        email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [attendeeEmail], connection=connection)
        email.send()
    resetGlobals()
    connection.close()

def sendItemsEmailUpdate(attendeeEmail,hostName, eventName,itemName):
    connection = mail.get_connection()
    connection.open()
    subject = "Item Modification"
    message = "Hello we are sorry to inform you that: " + hostName + " has changed the item: '" + itemName + " for event: "+ eventName + "\nAs a result of the change you have been automatically unsigned up for the item: "+ itemName +"\n"
    email = EmailMessage(subject,message,settings.DEFAULT_FROM_EMAIL, [attendeeEmail],connection=connection)
    email.send()
    resetGlobals()
    connection.close()