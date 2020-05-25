from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.handlelogin, name='login'),
    path('logout', views.handlelogout, name='logout'),

    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name = "client/reset_password/password_reset.html"),            #reset password
    name = "reset_password"),  

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name = "client/reset_password/password_reset_sent.html"),  #reset password in email
    name = "password_reset_done"), 

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name = "client/reset_password/password_reset_form.html"),       #confirm new password                                                           #confirm password
    name = "password_reset_confirm"),  

    path('reset_password_complete/',                              
    auth_views.PasswordResetCompleteView.as_view(template_name = "client/reset_password/password_reset_done.html"),        #reset completed                                                       #reset password
    name = "password_reset_complete"), 
]