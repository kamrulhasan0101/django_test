from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.


def index(request):
    return HttpResponse("this is accounts module root page")


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']
        if password == con_password:
            if User.objects.filter(email=email).exists():
                print("Email already exists !")
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                user.save()
                print("New User Created")
            return redirect('/')
        else:
            print("Password does not match")
            return redirect('/')
    else:
        return render(request, 'register.html')

