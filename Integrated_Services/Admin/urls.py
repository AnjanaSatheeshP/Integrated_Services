from django.urls import path
from Admin.views import *


urlpatterns=[
    path('',adminhome,name='adminhome'),
    path('admin_add_department/',admin_add_department,name='admin_add_department1'),
    path('admin/view_department/',view_department,name='view_department'),
    path('admin_department_edit/<id>',admin_department_edit,name='admin_department_edit'),
    path('department_update/<id>',admin_department_update,name='admin_department_update'),
    path('admin_department_delete/<id>',admin_department_delete,name='admin_department_delete'),
    
    path('admin_add_location/',admin_add_location,name='admin_add_location'),
    path('admin/view_location/',view_location,name='view_location'),
    path('admin_location_edit/<id>',admin_location_edit,name='admin_location_edit'),
    path('location_update/<id>',admin_location_update,name='admin_location_update'),
    path('admin_location_delete/<id>',admin_location_delete,name='admin_location_delete'),


    path('admin_add_Coordinator',admin_add_Coordinator,name='admin_add_Coordinator'),
    path('view_Coordinator',view_Coordinator,name='view_Coordinator'),
    path('admin_Coordinator_edit/<id>',admin_Coordinator_edit,name='admin_Coordinator_edit'),
    path('admin_Coordinator_delete/<id>',admin_Coordinator_delete,name='admin_Coordinator_delete'),
    path('admin_Coordinator_update/<id>',admin_Coordinator_update,name='admin_Coordinator_update'),
    
    
    path('view__user_JobApplications/',view__user_JobApplications,name='view__user_JobApplications'),
    path('view_user_payment_status/',view_user_payment_status,name='view_user_payment_status'),
    path('view__user_JobApplications_status/',view__user_JobApplications_status,name='view__user_JobApplications_status'),
    path('view_employee_to_assign/<id>',view_employee_to_assign,name='view_employee_to_assign'),
    path('assign_employee/<eid>/<jid>',assign_employee,name='assign_employee'),
    
    ]