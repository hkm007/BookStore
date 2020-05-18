from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'store/home.html')

def products(request):
    data = Book.objects.all()
    params = {'Book':data}
    return render(request, 'store/products.html',params)

def contact(request):
    return render(request, 'store/contact.html')