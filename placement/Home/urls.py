from django.urls import path
from .views import *


urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('student_reg/',student_reg,name='student_reg'),
    # path('ShopSignUp/',ShopSignUp,name='ShopSignUp'),
    path('SignIn/',SignIn,name='SignIn'),
    path('accounts_logout/',accounts_logout,name='accounts_logout'),
    
]