from django.urls import path
from .views import *


urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('user_reg/',user_reg,name='user_reg'),
    # path('ShopSignUp/',ShopSignUp,name='ShopSignUp'),
    path('SignIn/',SignIn,name='SignIn'),
    path('admin_signIn/',admin_signIn,name='admin_signIn'),
    path('Emp_SignIn/',Emp_SignIn,name='Emp_SignIn'),
    path('User_SignIn/',User_SignIn,name='User_SignIn'),
    path('accounts_logout/',accounts_logout,name='accounts_logout'),
    
]