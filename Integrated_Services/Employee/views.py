from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from Admin.models import Department
from Home.models import User,User_Details,Employee
from Customer.models import Job_Application
# from Student.models import Job_Application
from django.db.models import F
from django.db import connection 
# Create your views here.
from django.core.mail import send_mail  
from Integrated_Services import settings  
from datetime import datetime
from django.db.models import Count, Sum
from django.db import connection


def Employeehome(request):   
    eid=request.session['Employee_id']
    employee_id=User.objects.get(id=eid)
    status_counts = Job_Application.objects.filter(employee_assigned_id_id=employee_id).values('status').annotate(count=Count('status'))
    print('ss',status_counts)
    data={'OnGoing':0,"Completed":0,'Assigned':0,'Paid':0}
#     ........ {'status': 'Completed', 'count': 1}
# .......... {'status': 'Paid', 'count': 1}
    
    for i in status_counts:
        # if i['status']=="Paid":
        #     continue
        data[i['status']]=i['count']
    print('..........',data)
    tot_complt= data['Paid']+ data['Completed']
    
    fname=employee_id.first_name
    lname=employee_id.last_name
    name=fname+" "+lname
    return render(request,'Employee/home.html',{'data':data,'tot_complt':tot_complt,'name':name})

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

    
def view_assined_jobs(request):  
    if request.method=="GET":
        
        eid=request.session['Employee_id']
        employee_id=User.objects.get(id=eid)
        
        result = Job_Application.objects.filter(employee_assigned_id=employee_id).exclude(status__in=['Completed', 'Paid'])
        
        sql_query="""select Customer_job_application.id, first_name, last_name,email,Home_user_details.address, Home_user_details.lat,Home_user_details.lng,dept_name,
work_details,apply_date, work_date,status , employee_assigned_id_id
 from Customer_job_application 
join Home_user on Customer_job_application.user_id_id=Home_user.id
join Home_user_details on Home_user_details.user_id_id=Home_user.id
join Admin_department on Customer_job_application.department_id_id=Admin_department.id

where Customer_job_application.employee_assigned_id_id=%s and status not in ('Completed', 'Paid')"""  #join Admin_location on Home_user_details.loc_id_id= Admin_location.id

        with connection.cursor() as cursor:
            cursor.execute(sql_query,[eid])
            rows = dictfetchall(cursor)
        result=rows
        print(result,'...') 
            
        
        print(result)
        return render(request,'Employee/view_assined_jobs.html',{'result':result})   
    else:
        jid=request.POST['jid']
        status=request.POST['status']
        job = Job_Application.objects.get(id=jid) 
        job.status=status
        job.status_updated=datetime.now()
        job.save()
        return  redirect('view_assined_jobs')



def emp_view_completed_jobs(request):    
        
    eid=request.session['Employee_id']
    employee_id=User.objects.get(id=eid)
    result = Job_Application.objects.filter(employee_assigned_id=employee_id, status__in=['Completed', 'Paid'])
    print(result)
    return render(request,'Employee/view_completed_jobs.html',{'result':result})         

def emp_created_amount(request):
    
    eid=request.session['Employee_id']
    employee_id=User.objects.get(id=eid)
    
    total_emp_amount = Job_Application.objects.filter(employee_assigned_id=employee_id).aggregate(total=Sum('emp_amount'))
    print(total_emp_amount)
    result = Job_Application.objects.filter(employee_assigned_id=employee_id, status='Paid')
    print(result)
    #c=f"{total_emp_amount:.3f}"
    return render(request,'Employee/credit.html',{'data':total_emp_amount,'result':result})

def emp_editprofile(request):
    if request.method=="GET":
        eid=request.session['Employee_id']
        employee_id=Employee.objects.get(employee_id=eid)
        x=Department.objects.all()
        return render(request,'Employee/edit_profile.html',{'data':employee_id,'dept':x})
    else:
        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        salary=request.POST['salary']
        experience=request.POST['experience']
        # username=request.POST['username']
        # password=request.POST['password']
        
        department=request.POST['dept_id']
        department_id = Department.objects.get(dept_name=department) 
        
        eid=request.session['Employee_id']
        emp=Employee.objects.get(employee_id=eid)
        
        user=User.objects.get(id=eid)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        # username=username,
        # password=password
        # ,usertype='Employee',
        user.address=address
        user.phone_number=phone
        user.save()
        
        emp.department_id=department_id
        emp.address=address
        emp.phone_number=phone
        emp.salary=salary
        emp.experience=experience
        emp.save()
            
        return HttpResponse("<script>window.alert('Successfully Employee Profile Updated !!');window.location.href='/Employee/emp_editprofile/'</script>")
    
def emp_view_loc(request,lat,lng):
   
    print('lat -->',lat ,'lng -->',lng )
    return render(request,'Employee/view_loc.html',{'lat':lat,'lng':lng})       