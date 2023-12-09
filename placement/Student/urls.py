from django.urls import path
from Student.views import *


urlpatterns=[
    path('',Studenthome,name='Studenthome'),
    path('stud_view_Jobs/',stud_view_Jobs,name='stud_view_Jobs'),
    path('stud_apply_job/<id>',stud_apply_job,name='stud_apply_job'),
    path('view_res',view_res,name='view_res'),

    ]