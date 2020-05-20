from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Book
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from django.template.loader import render_to_string

def home(request):
    return render(request, 'store/home.html')

def products(request):
    data = Book.objects.all()
    params = {'Book':data}
    return render(request, 'store/products.html',params)

def contact(request):
    params  = {"msg_disp":False}
    if request.method == 'POST':
        userName = request.POST.get('UserName','')
        userEmail = request.POST.get('UserEmail','')
        userMsg = request.POST.get('UserMessage')
        template = render_to_string('store/contact_message.html',{'UserName':userName,'UserEmail':userEmail,'UserMsg':userMsg})
        email = EmailMessage(
            'Message from '+userName,
            template,
            settings.EMAIL_HOST_USER,
            ['deeprajbaiddya@gmail.com']
        )
        email.fail_silently = False
        email.send()
        params = {"msg_disp":True,"msg":"Your form has been submitted successfully."}
        return render(request,'store/contact.html',params)
    else:
        return render(request, 'store/contact.html',params)

def handlecontact(request):
    if request.method == 'POST':
        qname = request.POST.get('qname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        status = request.POST.get('status')

        # deepraj implement email logic here
        
        print(qname, email, message, status)  # just for testing

        messages.success(request, 'Your message has been sent successfully! Our team will contact you soon.')
        return redirect('contact')
    else:
        return HttpResponse('Error: 404 Not Found')