from django.shortcuts import render

# Create your views here.

def index_page(request):
	return render(request, 'booking/index.html')

def login_page(request):
	return render(request, 'booking/login.html')
	
def events_page(request):
	return render(request, 'booking/events.html')

def event_details_page(request):
	return render(request, 'booking/event-details.html')

def clubs_page(request):
	return render(request, 'booking/clubs.html')

def club_details_page(request):
	return render(request, 'booking/club-details.html')

def profile_details_page(request):
	return render(request, 'booking/profile-details.html')