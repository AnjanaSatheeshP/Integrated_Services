from django.urls import path
from Employee.views import *


urlpatterns=[
    path('',Employeehome,name='Employeehome'),
   
    path('view_assined_jobs/',view_assined_jobs,name='view_assined_jobs'),
    path('emp_view_completed_jobs/',emp_view_completed_jobs,name='emp_view_completed_jobs'),
    path('emp_created_amount/',emp_created_amount,name='emp_created_amount'),
    path('emp_editprofile/',emp_editprofile,name='emp_editprofile'),
    path('emp_view_loc/<lat>/<lng>',emp_view_loc,name='emp_view_loc'),
  

    ]