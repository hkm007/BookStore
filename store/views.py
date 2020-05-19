from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Book

def home(request):
    return render(request, 'store/home.html')

def products(request):
    data = Book.objects.all()
    params = {'Book':data}
    return render(request, 'store/products.html',params)

def contact(request):
    return render(request, 'store/contact.html')

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