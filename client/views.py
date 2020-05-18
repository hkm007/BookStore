from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(username, email, password)
        messages.success(request, 'Account Successfully created! Now you can login.')
        return redirect('home')
    else:
        return HttpResponse('Error: 404 Not Found')

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome! You are successfully logged in.')
        else:
            messages.warning(request, 'Invalid Credentials. Try again')
            
        return redirect('home')
    else:
        return HttpResponse('Error: 404 Not Found')

def handlelogout(request):
    logout(request)
    messages.success(request, 'You are successfully logged out.')
    return redirect('home')