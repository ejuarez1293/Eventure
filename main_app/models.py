from django.db import models
from django import forms
from django.contrib.auth.models import User
from localflavor.us.models import USStateField


class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name = 'user', on_delete='CASCADE')
	id = models.AutoField(primary_key = True)
	firstName = models.CharField(max_length = 50, default = '')
	lastName = models.CharField(max_length = 50, default = '')
	profilePhoto = models.ImageField(upload_to = 'profile_photos', blank = True, default = None)
	city = models.CharField(("city"), max_length=64)
	state = USStateField(("state"), default="TX")
	zip = models.CharField(("zip code"), max_length=5)

	def __str__(self):
		return self.firstName + ' ' + self.lastName

class EventInfo(models.Model):
	NONE = 0
	PARTY = 1
	EDUCATION = 2
	MUSIC = 3
	FOODDRINK = 4
	MOVIE = 5
	ARTS = 6
	TECH = 7
	HEALTH = 8
	OUTDOOR = 9
	SPORTS = 10
	
	EVENTCATEGORY = (
		(NONE,"Misc"),
		(PARTY, "Party"),
		(EDUCATION, "Education"),
		(MUSIC, "Music"),
		(FOODDRINK, "Food and Drink"),
		(MOVIE, "Movies"),
		(ARTS, "Arts"),
		(TECH, "Technology"),
		(HEALTH, "Health"),
		(OUTDOOR, "Out Doors"),
		(SPORTS, "Sports")
	
	)
	
	id = models.CharField(primary_key = True, max_length = 12, default = '')
	userProfile = models.ForeignKey(UserProfile, null = True, on_delete='CASCADE')
	type = models.BooleanField(default = False)  #auto-set to public
	name = models.CharField(max_length = 255, default = '')
	location = models.CharField(max_length = 255)
	date = models.DateField(null = True)
	time = models.TimeField(null = True)
	description = models.TextField()
	eventPhoto = models.ImageField(upload_to = 'event_photos', blank = True, default = None
	                               , verbose_name='picture')
	eventCategory = models.IntegerField(choices=EVENTCATEGORY, blank=True, null=True)


	def __str__(self):
		return '{} Hosted by {first} {last}'.format(self.name,
		                                       first = self.userProfile.firstName,
		                                       last = self.userProfile.lastName)


class Item(models.Model):
	itemID = models.AutoField(primary_key = True)
	eventID = models.ForeignKey(EventInfo, null = True, on_delete='CASCADE')
	name = models.CharField(max_length = 255, default = '')
	amount = models.IntegerField(default = 0)
	amountTaken = models.PositiveIntegerField(default=0)
	isTaken = models.BooleanField(default = False)

	def __str__(self):
		return '{} x {}'.format(self.name, self.amount)

	
class Attendee(models.Model):
	NOTATTENDING = 1
	MAYBE = 2
	ATTENDING = 3
	
	RSVPSTATUS = (
		(NOTATTENDING, "Not Attending"),
		(MAYBE, "Maybe"),
		(ATTENDING, "Attending"),
		
	)
	
	attendeeName = models.CharField(max_length=256, default = '')
	attendeeID = models.CharField(max_length = 8, default = '')
	userAttendeeID = models.IntegerField(null = True)
	eventID = models.ForeignKey(EventInfo, null = True, on_delete='CASCADE')
	email = models.EmailField(max_length=256, default='')
	RSVPStatus = models.IntegerField(choices=RSVPSTATUS, blank=True, null=True)
	
	def __str__(self):
		return '{}'.format(self.attendeeName)


class TakenItem(models.Model):
	itemBeingBroughtID = models.AutoField(primary_key=True)
	attendeeID = models.ForeignKey(Attendee, on_delete='CASCADE')
	itemLinkID = models.ForeignKey(Item, on_delete='CASCADE')
	eventID = models.ForeignKey(EventInfo, on_delete='CASCADE')
	quantity = models.PositiveIntegerField(default=0)
	comment = models.TextField(default='')

	def __str__(self):
		return '{} x {} is being brought by {} '.format(self.itemLinkID.name,
		                                                self.quantity, self.attendeeID.attendeeName)


class Poll(models.Model):
	pollID = models.AutoField(primary_key=True)
	question = models.CharField(max_length=200)
	eventID = models.ForeignKey(EventInfo, null=True, on_delete='CASCADE')
	def __str__(self):
		return '{}'.format(self.question)

class Choice(models.Model):
	poll = models.ForeignKey(Poll, on_delete='CASCADE')
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return '{}'.format(self.choice_text,self.poll,self.votes)

class voter(models.Model):
	poll = models.ForeignKey(Poll, on_delete='CASCADE')
	attendeeID = models.ForeignKey(Attendee, on_delete='CASCADE')
	
	def __str__(self):
		return '{}'.format(self.attendeeID,self.poll)