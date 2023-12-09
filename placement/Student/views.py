from django.shortcuts import render
from Coordinator.models import Job,Resource
from Home.models import Student
from Student.models import Job_Application
from django.http.response import HttpResponse

# Create your views here.
from datetime import date

from django.db.models import F, Q, Max

def Studenthome(request):
   
    return render(request,'Student/home.html')


def stud_view_Jobs(request):     
    
    stud =request.session.get('studid')
    
    print(stud)
    student=Student.objects.get(student_id_id=stud)
    
    
    current_date = date.today()
    target_student_id = stud
    
    details = Job.objects.filter(
    department_id__student__cgpa__gte=F('cgpa'),
    department_id__student__back_logs__lte=F('back_logs'),
    last_date__gte=current_date,
    department_id__student__student_id=target_student_id
).values(
    'id','CompanyName', 'post', 'no_of_vacancy', 'cgpa', 'back_logs','department_id__dept_name',"package","bond","last_date",
).annotate(
    last_job_date=Max('last_date')
).filter(
    last_job_date__gte=current_date
)

    print(details)
    return render(request,'student/stud_view_Jobs.html',{'data':details})    



def stud_apply_job(request,id):
    print('.........................')
    stud =request.session.get('studid')    
    print(stud)
    student=Student.objects.get(student_id_id=stud)
    
    job_id= Job.objects.get(id=id)
    
    
    exists = Job_Application.objects.filter(student_id=student,job_id=job_id)
    
    if exists:
        return HttpResponse("<script>window.alert('Alredy Applied For Job !!');window.location.href='/Student/stud_view_Jobs/'</script>") 
    else:
        jop_apply=Job_Application.objects.create(student_id=student,
                                job_id=job_id )
        jop_apply.save()
        
        return HttpResponse("<script>window.alert('Successfully Applied For Job !!');window.location.href='/Student/stud_view_Jobs/'</script>")
    
    
def view_res(request):  
    result = Resource.objects.select_related('department_id').select_related('department_id')
    print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,',result)
    return render(request,'student/view_resource.html',{'result':result})       