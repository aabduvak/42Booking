from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
	path('', views.index_page, name="index"), # https://42booking.com.tr/
	path('login', views.login_page, name='login'),
	path('events', views.events_page, name='event-list'),
	path('events/<slug:slug>', views.event_details_page, name='event-detail'),
	path('clubs', views.clubs_page, name='club-list'),
	path('clubs/<slug:slug>', views.event_details_page, name='club-details'),
	path('profile/<str:username>', views.profile_details_page, name='profile'),
]