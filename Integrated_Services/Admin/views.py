from django.shortcuts import render,redirect
from django.http.response import HttpResponse
# Create your views here.
from Admin.models import Department #,Location
from Home.models import  User,Employee,User_Details
from Customer.models import  Job_Application

from django.http import JsonResponse
from django.db.models import Count,Sum
from django.db import connection
# from Teacher.models import Student_Academic



def adminhome(request):
    
    status_counts = Job_Application.objects.values('status').annotate(count=Count('status'))
    print(status_counts)
    data={'Paid':0,'OnGoing':0,"Completed":0,'Pending':0,'Assigned':0 }
    
    for i in status_counts:
       
        data[i['status']]=i['count']
    print('..........',data)
    
    totals = Job_Application.objects.aggregate(
        total_paid_amount=Sum('paid_amount'),
        total_emp_amount=Sum('emp_amount'),
        total_comm_amount=Sum('comm_amount')
    )
    
    tot_complt= data['Paid']+ data['Completed']
   
    return render(request,'admin/home.html',{'data':data,'totals':totals,'tot_complt':tot_complt})

def emp_dash(request):
   
    return render(request,'admin/emp_dashboard.html')


def admin_add_department(request):
    # if request.session.has_key('forValidation'):
    if request.method=="GET":
        return render(request,'admin/add_department.html')
    else:
        dname=request.POST.get('dept_name')   
        
        entry_exists = Department.objects.filter(dept_name=dname).exists()
        
        if entry_exists:
            return HttpResponse("<script>window.alert(' Work Type already Exist !!');window.location.href='/adminapp/admin_add_department/'</script>")
        else:    
            dept=Department()
            dept.dept_name=dname
        
            dept.save()
      
            return HttpResponse("<script>window.alert('Successfully Work Type Added!!');window.location.href='/adminapp/admin_add_department/'</script>")
    # else:
    #     return redirect('logouts')   


def view_department(request):    
    dept=Department.objects.all()
    return render(request,'admin/view_department.html',{'data':dept})



def admin_department_delete(request,id):
    dept = Department.objects.get(id=id)  
    dept.delete()  
    return redirect("view_department") 


def admin_department_edit(request,id):
    dept = Department.objects.get(id=id)  
    return render(request,'admin/edit_department.html', {'dept':dept})  

def admin_department_update(request, id):    
        dept = Department.objects.get(id=id)  
        dept.dept_name=request.POST.get('dept_name')
       
        dept.save()
        
        return redirect("view_department")     
    
    
def admin_add_Coordinator(request):
    if request.method=="GET":
        x=Department.objects.all()
        return render(request,'admin/add_Coordinator.html',{'dept':x})      
    else:
        department=request.POST['dept_id']
        department_id = Department.objects.get(id=department) 
       
        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        salary=request.POST['salary']
        experience=request.POST['experience']
        username=request.POST['username']
        password=request.POST['password']
        
        if  User.objects.filter(username=username).exists():
            return HttpResponse("<script>window.alert('Username alredy Exist!!');window.location.href='/adminapp/admin_add_Coordinator'</script>")
            
        else:
            new_user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,
                                            password=password,usertype='Employee',address=address,phone_number=phone)
            new_user.save()
            
            tech=Employee.objects.create(employee_id=new_user,department_id=department_id,
                                        address=address,phone_number=phone,
                                    salary=salary,experience=experience )
            tech.save()
            
            return HttpResponse("<script>window.alert('Successfully Employee Details Added!!');window.location.href='/adminapp/admin_add_Coordinator'</script>")  
    
    
    

def view_Coordinator(request):    
    
    if request.method=="POST":
        department=request.POST['dept_id']
        department_id = Department.objects.get(id=department) 
        x=Department.objects.all()
        details = Employee.objects.filter(department_id=department_id)
        return render(request,'admin/view_Coordinator.html',{'data':details,'dept':x})
        
    else:
        x=Department.objects.all()
        details = Employee.objects.select_related('employee_id','department_id')
        return render(request,'admin/view_Coordinator.html',{'data':details,'dept':x})

def admin_Coordinator_edit(request,id):
   
    details = Coordinator.objects.select_related('Coordinator_id').filter(id=id)
    return render(request,'admin/edit_Coordinator.html',{'data':details})

    
def admin_Coordinator_delete(request,id):
    tech=Employee.objects.get(id=id)
    tech.delete()
    # return redirect('view_Coordinator')
    return HttpResponse("<script>window.alert('Successfully Employee  Deleted!!');window.location.href='/adminapp/view_Coordinator'</script>")  

def admin_Coordinator_update(request,id):
    tech = Coordinator.objects.get(id=id)
    uid=tech.Coordinator_id_id
    user=User.objects.get(id=uid)
    


    user.first_name=request.POST['first_name']
    user.last_name=request.POST['last_name']
    user.email=request.POST['email']
    tech.address=request.POST['address']
    tech.phone_number=request.POST['phone']
    tech.salary=request.POST['salary']
    tech.experience=request.POST['experience']
    tech.save()
    user.save()
    
    return redirect('view_Coordinator')      

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def view__user_JobApplications(request):  
    # result = Job_Application.objects.select_related('department_id').select_related('department_id').order_by('last_date')
    
#     result=Job_Application.objects.filter(status='Pending').select_related(
#     'user_id', 'department_id','user_id_id__User_Details__loc_id'
# ).prefetch_related(
#     'user_id__User_Details'
# )
    
    
#     result=Job_Application.objects.filter(status='Pending').select_related(
#     'user_id', 'department_id'
# ).prefetch_related(
#     'user_id_id__User_Details'
# )
    # result = Job_Application.objects.filter(status='Pending') \
    #     .select_related('user_id')
    # print(result)
    # Access fields from related models
    # for application in queryset:
    #     print(application.user_id.address)  # Example access to related field
    #     print(application.user_id.user_details.loc_id.loc_name) 
            
    sql_query="""select Customer_job_application.id as id, first_name, last_name,email,Home_user_details.address, Home_user_details.lat,Home_user_details.lng,dept_name,
work_details,apply_date, work_date,status
 from Customer_job_application 
join Home_user on Customer_job_application.user_id_id=Home_user.id
join Home_user_details on Home_user_details.user_id_id=Home_user.id
join Admin_department on Customer_job_application.department_id_id=Admin_department.id

where status='Pending'"""      #join Admin_location on Home_user_details.loc_id_id= Admin_location.id
    
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = dictfetchall(cursor)
    result=rows
    print(result,'...')        
    return render(request,'admin/view__user_JobApplications.html',{'result':result})   


def view_employee_to_assign(request,id):    
    
    job_details=Job_Application.objects.get(id=id)    
    job_depat=job_details.department_id    
    print(job_depat)   
    
    
    employees=Employee.objects.filter(department_id=job_depat).select_related('employee_id').order_by('-rating')

    return render(request,'admin/assign_employee.html',{'data':employees,'job':id})   


def assign_employee(request,eid,jid): 
    
    emp=User.objects.get(id=eid)
    
    job=Job_Application.objects.get(id=jid)
    job.status='Assigned'
    job.employee_assigned_id=emp
    job.save()
    
    return redirect('view__user_JobApplications')





def view__user_JobApplications_status(request):  
    # result = Job_Application.objects.select_related('department_id').select_related('department_id').order_by('last_date')
    if request.method=="POST":
        status=request.POST['status']
        result = Job_Application.objects.filter(status=status).select_related(
    'user_id', 'department_id'
).prefetch_related(
    'user_id_id__User_Details'
)
       
        return render(request,'admin/view__user_JobApplications_status.html',{'result':result})
        
    else:
        result=Job_Application.objects.select_related(
        'user_id', 'department_id'
    ).prefetch_related(
        'user_id_id__User_Details'
    )
        print(result)
        return render(request,'admin/view__user_JobApplications_status.html',{'result':result})   

def view_user_payment_status(request):  
    # result = Job_Application.objects.select_related('department_id').select_related('department_id').order_by('last_date')
    
    result=Job_Application.objects.filter(status='Paid').select_related(
    'user_id', 'department_id'
).prefetch_related(
    'user_id_id__User_Details'
)
    print(result)
    return render(request,'admin/view_user_payment_status.html',{'result':result})   

#############  loc

def admin_add_location(request):
    # if request.session.has_key('forValidation'):
    if request.method=="GET":
        return render(request,'admin/add_location.html')
    else:
        lname=request.POST.get('loc_name')   
        
        entry_exists = Location.objects.filter(loc_name=lname).exists()
        
        if entry_exists:
            return HttpResponse("<script>window.alert(' Location already Exist !!');window.location.href='/adminapp/admin_add_location/'</script>")
        else:    
            loc=Location()
            loc.loc_name=lname
        
            loc.save()
      
            return HttpResponse("<script>window.alert('Successfully Location Added!!');window.location.href='/adminapp/admin_add_location/'</script>")
    # else:
    #     return redirect('logouts')   


def view_location(request):    
    loc=Location.objects.all()
    return render(request,'admin/view_location.html',{'data':loc})



def admin_location_delete(request,id):
    loc = Location.objects.get(id=id)  
    loc.delete()  
    # return redirect("view_location") 
    return HttpResponse("<script>window.alert('Successfully Location Deleted !!');window.location.href='/adminapp/admin_add_location/'</script>")


def admin_location_edit(request,id):
    loc = Location.objects.get(id=id)  
    return render(request,'admin/edit_location.html', {'loc':loc})  

def admin_location_update(request, id):    
    loc = Location.objects.get(id=id)  
    loc.loc_name=request.POST.get('loc_name')
    
    loc.save()
    return HttpResponse("<script>window.alert('Successfully Location Updated !!');window.location.href='/adminapp/admin_add_location/'</script>")
        # return redirect("view_department")    



