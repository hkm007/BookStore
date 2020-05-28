from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path("products/<int:my_id>",views.productView,name= "productView"),
    path('products/filter/', views.handlefilter, name='books-filter'),
    path('contact/', views.contact, name='contact'),
    path('checkout/<int:x_id>', views.checkout, name='checkout'),
    path('addbook/', views.addBook, name='addBook'),
    path('contact/post', views.handlecontact, name='contact-post'),
    path('handlerequest/', views.handleRequest, name='handleRequest'),
]