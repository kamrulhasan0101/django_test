from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'Kamrul Hasan'})


def add(request):
    if request == 'POST':
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        result = val1 + val2
        return render(request, 'result.html', {'result': result})
    else:
        return render(request, 'home.html')
