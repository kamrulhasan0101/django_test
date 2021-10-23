from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.


def index(request):
    event1 = Event('pic1', '22')
    event2 = Event('pic2', '33')
    event3 = Event('pic3', '44')
    event4 = Event('pic4', '55')
    events = [event1, event2, event3, event4]
    return render(request, 'index.html', {'events': events})
