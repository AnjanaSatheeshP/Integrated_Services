from django.urls import path
from Customer.views import *


urlpatterns=[
    path('',Customerhome,name='Customerhome'),
  
    path('cust_apply_job/',cust_apply_job,name='cust_apply_job'),
    path('view_job_applications/',view_job_applications,name='view_job_applications'),
    path('view_completed_jobs/',view_completed_jobs,name='view_completed_jobs'),
    path('feedback_rating_completed_jobs/',feedback_rating_completed_jobs,name='feedback_rating_completed_jobs'),
    path('cust_editprofile/',cust_editprofile,name='cust_editprofile'),
    path('cust_set_loc/',cust_set_loc,name='cust_set_loc'),
    path('del_apply_job_byUser/<int:id>',del_apply_job_byUser,name='del_apply_job_byUser'),
    path('cust_feedback/<int:id>',cust_feedback,name='cust_feedback'),
    path('cust_rating/<int:id>',cust_rating,name='cust_rating'),

    path('cust_pay/<int:jid>/<int:eid>',cust_pay, name='cust_pay'),
    path('success/<int:jid>/<int:amount>',success, name='success'),

    ]