from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path("products/<int:my_id>",views.productView,name= "productView"),
    path('books/filter', views.handlefilter, name='books-filter'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('addbook/', views.addBook, name='addBook'),
    path('contact/post', views.handlecontact, name='contact-post'),
]