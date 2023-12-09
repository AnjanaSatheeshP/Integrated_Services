from django.shortcuts import render,redirect
from django.http.response import HttpResponse
# Create your views here.
from Admin.models import Department,Courses
from Home.models import  User,Coordinator

from django.http import JsonResponse
# from Teacher.models import Student_Academic



def adminhome(request):
   
    return render(request,'admin/home.html')


def admin_add_department(request):
    # if request.session.has_key('forValidation'):
    if request.method=="GET":
        return render(request,'admin/add_department.html')
    else:
        dept=Department()
        dept.dept_name=request.POST.get('dept_name')   
        
        dept.save()
      
        return HttpResponse("<script>window.alert('Successfully Department Added!!');window.location.href='/adminapp/admin_add_department/'</script>")
    # else:
    #     return redirect('logouts')   


def view_department(request):    
    dept=Department.objects.all()
    return render(request,'admin/view_department.html',{'data':dept})

def view_course(request):    
    course=Courses.objects.select_related('department_id')
    return render(request,'admin/view_Course.html',{'data':course})

def admin_course_edit(request,id):
    pass

def admin_course_delete(request,id):
    course=Courses.objects.get(id=id)
    course.delete()
    return redirect('view_course')

def admin_course_update(request,id):
    pass


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
    
       
        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        salary=request.POST['salary']
        experience=request.POST['experience']
        username=request.POST['username']
        password=request.POST['password']
        
        
        new_user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,
                                          password=password,usertype='Coordinator')
        new_user.save()
        
        tech=Coordinator.objects.create(Coordinator_id=new_user,
                                    address=address,phone_number=phone,
                                   salary=salary,experience=experience )
        tech.save()
        
        return HttpResponse("<script>window.alert('Successfully Coordinator Details Added!!');window.location.href='/adminapp/admin_add_Coordinator'</script>")  
    
    
    

def view_Coordinator(request):    
    details = Coordinator.objects.select_related('Coordinator_id')
    return render(request,'admin/view_Coordinator.html',{'data':details})

def admin_Coordinator_edit(request,id):
   
    details = Coordinator.objects.select_related('Coordinator_id').filter(id=id)
    return render(request,'admin/edit_Coordinator.html',{'data':details})

    
def admin_Coordinator_delete(request,id):
    tech=Coordinator.objects.get(id=id)
    tech.delete()
    return redirect('view_Coordinator')

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
