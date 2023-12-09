from django.urls import path
from Coordinator.views import *


urlpatterns=[
    path('',Coordinatorhome,name='Coordinatorhome'),
    path('add_Jobs/',add_Jobs,name='add_Jobs'),
    path('view_jobs/',view_jobs,name='view_jobs'),
    path('view_applications/<id>',view_applications,name='view_applications'),
    path('add_Resources/',add_Resources,name='add_Resources'),

    ]