from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from Admin.models import Department
from Home.models import User,Student
from Coordinator.models import Job,Resource
from Student.models import Job_Application
from django.db.models import F
from django.db import connection 
# Create your views here.
from django.core.mail import send_mail  
from placement import settings  
def Coordinatorhome(request):   
    return render(request,'Coordinator/home.html')



def add_Jobs(request):
    if request.method=="GET":
        x=Department.objects.all()
        return render(request,'Coordinator/add_Jobs.html',{'dept':x})   
    else:
        department=request.POST['dept_id']
        department_id = Department.objects.get(id=department) 
        
        CompanyName=request.POST['CompanyName']
        post=request.POST['post']
        no_of_vacancy=request.POST['no_of_vacancy']
        cgpa=request.POST['cgpa']
        back_logs=request.POST['back_logs']
        last_date=request.POST['last_date']
        package=request.POST['package']
        bond=request.POST['bond']
       
        
        job=Job.objects.create(department_id=department_id,CompanyName=CompanyName,
                                    cgpa=cgpa,back_logs=back_logs,post=post,no_of_vacancy=no_of_vacancy,
                                   last_date=last_date,bond=bond, package=package)
        job.save()   



        # std= Student.objects.filter(department_id=department_id)
        std=Student.objects.filter(department_id_id=department_id).select_related('student_id').values('student_id__email')
        print(std)
        
        for i in std:
            print(i["student_id__email"])
            subject = "New JOb Offer"  
            msg     = "Congratulations New Offer For You"  
            to      = i["student_id__email"]
            res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
        
        
        return HttpResponse("<script>window.alert('Successfully Job Post Added!!');window.location.href='/Coordinator/add_Jobs/'</script>")
    
    
def view_jobs(request):  
    result = Job.objects.select_related('department_id').select_related('department_id').order_by('last_date')
    print(result)
    return render(request,'Coordinator/view_jobs.html',{'result':result})   



def dictfetchall(id):
 
    "Return all rows from a cursor as a dict"
    with connection.cursor() as cursor:
       
        cursor.execute("""  select 
Home_user.first_name, Home_user.last_name,Home_user.email,Home_student.back_logs,Home_student.cgpa, 
Home_student.sslc,Home_student.plus_two,Home_student.cv,Home_student.photo 
from  Student_job_application join Coordinator_job   on Coordinator_job.id= Student_job_application.job_id_id 
join Home_student on Home_student.id=Student_job_application.student_id_id 
join Home_user on Home_user.id=Home_student.student_id_id where job_id_id= %s;                         
                                """, (id,))
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
  
  
def view_applications(request,id):
    
    print(',,,,,,,,,,,,,,,,,,,',id)
#     result = Job_Application.objects.filter(
#     student_id__id=F('student_id__id'),
#     job_id_id=id
# ).select_related('student_id', 'student_id__department_id')


    # result = CoordinatorJob.objects.filter(   
    #     student_job_application__job_id_id=id
    # ).select_related('student_job_application', 'student_job_application__student_id', 'student_job_application__student_id__student_id')
        
        
        
    result=dictfetchall(id)
    print(result)
        
        
    
    return render(request,'Coordinator/view_applications.html',{'result':result}) 
    
    
    

def add_Resources(request):
    if request.method=="GET":
        x=Department.objects.all()
        return render(request,'Coordinator/add_resources.html',{'dept':x})   
    else:
        department=request.POST['dept_id']
        department_id = Department.objects.get(id=department) 
        
        re_s=request.FILES['re_s']
        topic=request.POST['topic']    
        resource=Resource.objects.create(department_id=department_id,res=re_s,
                                    topic=topic)
        resource.save()   
        
        return HttpResponse("<script>window.alert('Successfully Job Post Added!!');window.location.href='/Coordinator/add_Resources/'</script>")
    