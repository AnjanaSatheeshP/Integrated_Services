from django.urls import path
from Admin.views import *


urlpatterns=[
    path('',adminhome,name='adminhome'),
    path('admin_add_department/',admin_add_department,name='admin_add_department1'),
    path('admin/view_department/',view_department,name='view_department'),
    path('admin_department_edit/<id>',admin_department_edit,name='admin_department_edit'),
    path('department_update/<id>',admin_department_update,name='admin_department_update'),
    path('admin_department_delete/<id>',admin_department_delete,name='admin_department_delete'),

    # path('admin_add_student',admin_add_student,name='admin_add_student'),    
    # path('get_second_dropdown_data/',get_second_dropdown_data ,name='hi'),
    # path('admin_manage_QR',admin_manage_QR,name='admin_manage_QR'),
    # path('admin_gen_QR/<id>',admin_gen_QR,name='admin_gen_QR'),
    # path('admin_view_QRcode_details',admin_view_QRcode_details,name='admin_view_QRcode_details'),
    # path('admin_view_academic_details/<id>',admin_view_academic_details,name='admin_view_academic_details'),
    path('admin_add_Coordinator',admin_add_Coordinator,name='admin_add_Coordinator'),
    path('view_Coordinator',view_Coordinator,name='view_Coordinator'),
    path('admin_Coordinator_edit/<id>',admin_Coordinator_edit,name='admin_Coordinator_edit'),
    path('admin_Coordinator_delete/<id>',admin_Coordinator_delete,name='admin_Coordinator_delete'),
    path('admin_Coordinator_update/<id>',admin_Coordinator_update,name='admin_Coordinator_update'),
    ]