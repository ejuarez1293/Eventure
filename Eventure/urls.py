"""Eventure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main_app import views
from django.views.static import serve
from Eventure import settings
from main_app.views import attendeeEventDisplay
urlpatterns = [
	url(r'^$',views.newIndex,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^event/(\w{12})(\w{8})$', attendeeEventDisplay.as_view()),
	url(r'^media/(?P<path>.*)$',serve , {'document_root': settings.MEDIA_ROOT, }),
    url(r'^createEvent$', views.createEvent, name = 'CreateEvent'),
	url(r'^landingPage$', views.landingPageView, name = 'Home'),
	url(r'^myEventsPage$', views.myEventsPageView, name = 'myEvents'),
	url(r'^register/$',views.register, name='registrationPage'),
    url(r'^userLogin/$',views.userLogin,  name='userLogin'),
	url(r'^SearchEvent/$',views.SearchEvent,  name='searchevent'),
    url(r'^logout/$',views.userLogout, name='logout'),
	url(r'^event/(\w{12})/$',views.eventHomePageView,name = 'eventHome'),
	url(r'^event/(\w{12})/edit$', views.edit, name='eventEdit'),
]
