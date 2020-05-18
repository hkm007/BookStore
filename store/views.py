from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return render(request, 'store/home.html')

def products(request):
    return render(request, 'store/products.html')

def contact(request):
    return render(request, 'store/contact.html')

def handlecontact(request):
    if request.method == 'POST':
        qname = request.POST.get('qname')
        qemail = request.POST.get('qemail')
        qmessage = request.POST.get('qmessage')
        qstatus = request.POST.get('qstatus')

        print(qname, qemail, qmessage, qstatus)
        messages.success(request, 'Your message has been sent successfully! Our team will get back to you soon.')
        return redirect('contact')

    else:
        return HttpResponse('Error: 404 Not Found')
