from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(EventInfo)
admin.site.register(Item)
admin.site.register(Attendee)
admin.site.register(TakenItem)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(voter)
