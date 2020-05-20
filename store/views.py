from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from django.template.loader import render_to_string
import requests
import json

def home(request):
    return render(request, 'store/home.html')

def products(request):
    data = Book.objects.all()
    params = {'Book':data}
    return render(request, 'store/products.html',params)

def contact(request):
    # params  = {"msg_disp":False}
    # if request.method == 'POST':
    #     userName = request.POST.get('UserName','')
    #     userEmail = request.POST.get('UserEmail','')
    #     userMsg = request.POST.get('UserMessage')
    #     template = render_to_string('store/contact_message.html',{'UserName':userName,'UserEmail':userEmail,'UserMsg':userMsg})
    #     email = EmailMessage(
    #         'Message from '+userName,
    #         template,
    #         settings.EMAIL_HOST_USER,
    #         ['deeprajbaiddya@gmail.com']
    #     )
    #     email.fail_silently = False
    #     email.send()
    #     params = {"msg_disp":True,"msg":"Your form has been submitted successfully."}
    #     return render(request,'store/contact.html',params)
    # else:
    return render(request, 'store/contact.html')

def handlecontact(request):
    if request.method == 'POST':
        qname = request.POST.get('qname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        status = request.POST.get('status')

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
            # deepraj implement email logic here
            template = render_to_string('store/contact_message.html',{'UserName':qname,'UserEmail':email,'UserMsg':message})
            email = EmailMessage(
                'Message from '+qname,
                template,
                settings.EMAIL_HOST_USER,
                ['pingoo.techie@gmail.com']
            )
            email.fail_silently = False
            email.send()
            print(qname, email, message, status)  # just for testing
            messages.success(request, 'Your message has been sent successfully! Our team will contact you soon.')
        else:
            messages.warning(request, 'reCaptcha not verified!')
        return redirect('contact')
    else:
        return HttpResponse('Error: 404 Not Found')

def cart(request):
    if request.user.is_authenticated:
        return render(request, 'store/cart.html')
    else:
        return HttpResponse('Error: 404 Not Found')
    