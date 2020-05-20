from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests
import json

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        clientkey = request.POST.get('g-recaptcha-response')
        secretkey = "6LcMOvoUAAAAADVKv88IJc9zJzH-5jgO_oFiwRN0"

        captchaData = {
            "secret": secretkey,
            "response": clientkey
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)
        verify = response['success']

        if verify:
            # logic for same username and email to be implemented
            User.objects.create_user(username, email, password)
            messages.success(request, 'Account Successfully created! Now you can login.')
        else:
            messages.warning(request, 'reCaptcha not verfied!')
        
        return redirect('home')
    else:
        return HttpResponse('Error: 404 Not Found')

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        clientkey = request.POST.get('g-recaptcha-response')
        secretkey = "6LcMOvoUAAAAADVKv88IJc9zJzH-5jgO_oFiwRN0"

        captchaData = {
            "secret": secretkey,
            "response": clientkey
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)
        verify = response['success']

        if verify:
            user = authenticate(username = loginusername, password = loginpassword)

            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome! You are successfully logged in.')
                return redirect('products')
            else:
                messages.warning(request, 'Invalid Credentials. Try again')

        else:
            messages.warning(request, 'reCaptcha not verified!')
            
        return redirect('home')
    else:
        return HttpResponse('Error: 404 Not Found')

def handlelogout(request):
    logout(request)
    messages.success(request, 'You are successfully logged out.')
    return redirect('home')