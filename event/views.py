from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.


def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})
