from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotFound,JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import requests
import json
from .book_form import BookForm
import datetime
from .models import Book,Order
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum

MERCHANT_ID = 'waIdeK60246441539675'
MERCHANT_KEY = 'byJM9Ilhn0O2uH6_'


def home(request):
    return render(request, 'store/home.html')

def products(request):
    data = Book.objects.all()
    params = {'Book':data}
    return render(request, 'store/products.html',params)

def productView(request,my_id):
    if request.user.is_authenticated:
        data = Book.objects.get(book_id = my_id)
        params = {"product":data}
        return render(request,'store/productView.html',params)
    else:
        messages.warning(request, 'You must be logged in.')
        return redirect('products')
        

def handlefilter(request):
    if request.method == 'POST':
        # branches = ['ALL','CSE','ECE','EE','EI','ME','PE','CHE & BE','BSMS & BTMT']
        branchSelected = request.POST.get('branchSelect')
        params = {}
        if (branchSelected == 'ALL'):
            allBook = Book.objects.all()
            params = {"branch":branchSelected,"Book":allBook}
        else:
            filtered_books = Book.objects.filter(book_branch = branchSelected)
            params = {"branch":branchSelected,"Book":filtered_books}
        return render(request,'store/products.html',params)
    else:
        return HttpResponse('Error: 404 Not Found')

def contact(request):
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

def checkout(request, x_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            book_name = request.POST.get('bookName')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            emailUser = request.POST.get('emailUser')
            phone = request.POST.get('userPhone')
            address = request.POST.get('userAddr')
            qty = request.POST.get('qty')
            totalAmt = request.POST.get('tot')

            newOrder = Order(book_name = book_name,fname = fname,lname = lname,email = emailUser,phone = phone,address = address,qty = qty,total = totalAmt)
            newOrder.save()

            param_dict = {
                'MID': MERCHANT_ID,
                'ORDER_ID':str(newOrder.order_id),
                'TXN_AMOUNT':str(newOrder.total),
                'CUST_ID':newOrder.email,
                'INDUSTRY_TYPE_ID':'Retail',
                'WEBSITE':'WEBSTAGING',
                'CHANNEL_ID':'WEB',
                'CALLBACK_URL':'http://localhost:8000/handlerequest/',
            }

            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
            return render(request,'store/paytm.html',{"param_dict":param_dict})
        else:
            data = Book.objects.get(book_id = x_id)
            params = {"product":data}
            return render(request, 'store/checkout.html', params)
    else:
        messages.warning(request, 'You must be logged in.')
        return redirect('products')


######################  Payment Gateway #############################

@csrf_exempt
def handleRequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if(i == 'CHECKSUMHASH'):
            checksum = form[i]
    
    verify = Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)

    if verify:
        if response_dict['RESPCODE'] == '01':
            print("ORDER SUCCESSFULY SUBMITTED")
        else:
            print("ORDER FAILURE" + response_dict['RESPMSG'])
    return render(request,'store/payment_status.html',{"response":response_dict})





###################### This is for admin only ########################

def addBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("saved successfully--------------------------------------------------------------------")
            form = BookForm()
            msg = "The form has been submitted successfully"
            params = {"form":form,"msg":msg}
            return render(request,'store/addBook.html',params)
        else:
            return HttpResponseNotFound("OOps Page not Found")
    else:
        form = BookForm()
        msg = False
        params = {"form":form,"msg":msg}
        return render(request,'store/addBook.html',params)
    