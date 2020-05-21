from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('contact/post', views.handlecontact, name='contact-post'),
    path('books/filter', views.handlefilter, name='books-filter'),
]