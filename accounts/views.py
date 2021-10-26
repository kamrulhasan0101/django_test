from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


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
                messages.info(request, "Email already exists !")
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                user.save()
                messages.info(request, "Registration Successful. Please login ")
                return redirect('accounts:login')
        else:
            messages.info(request, "Password does not match")
            return redirect('accounts:register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print("User authenticated")
            auth.login(request, user)
            return redirect('add')
        else:
            print("User not authenticated")
            messages.info(request, "Password does not match")
            return redirect('accounts:login')
    else:
        return render(request, 'login.html')
