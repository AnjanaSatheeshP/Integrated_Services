from django.shortcuts import  render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from Admin.models import Department
from Home.models import User,Student



def home(request):   
    return render(request,'Home/home.html')
def about(request):   
    return render(request,'Home/about.html')
def contact(request):   
    return render(request,'Home/contact.html')


def SignIn(request):
    print('...................')
    if request.method == 'GET':
        context = {}
        context['form'] = ''
        return render(request,'Home/SignIn.html',context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
      
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("adminhome")
            else:
                if user.usertype == 'student': # student
                    request.session["studid"]=user.id
                    
                    return redirect("Studenthome")
                elif user.usertype == "Coordinator": # Coordinator
                        login(request,user)
                        request.session['Coordinator_id']=user.id 
                        
                        return redirect("Coordinatorhome")
                else:
                    print('................')
                    return HttpResponse("<script>window.alert('INvalid!');window.location.href='/SignIn/'</script>")
               
        else:
            context = {}
            context['error'] = 'Invalid User or Admin not approved'
            return HttpResponse("<script>window.alert('INvalid!');window.location.href='/SignIn/'</script>")
        
   
    return HttpResponse("<script>window.alert('INvalid!');window.location.href='/SignIn/'</script>")


def student_reg(request):
  
    if request.method=="GET":
        x=Department.objects.all()
        return render(request,'Home/reg_Student.html',{'dept':x})      
    else:
        department=request.POST['dept_id']
        department_id = Department.objects.get(id=department) 
        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        cgpa=request.POST['cgpa']
        back_logs=request.POST['back_logs']
        sslc=request.POST['sscl']
        plus_two=request.POST['plus_two']
        DOB=request.POST['DOB']
        photo=request.FILES['photo']
        cv=request.FILES['cv']
       
        username=request.POST['username']
        password=request.POST['password']
        
        
        new_user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,
                                          password=password,usertype='student')
        new_user.save()
        
        stud=Student.objects.create(student_id=new_user,department_id=department_id,
                                    cgpa=cgpa,back_logs=back_logs,address=address,phone_number=phone,
                                   DOB=DOB,sslc=sslc,plus_two=plus_two,photo=photo,cv=cv )
        stud.save()


        return HttpResponse("<script>window.alert('Successfully Student Registered!!');window.location.href='/student_reg/'</script>")



def accounts_logout(request):
    logout(request)
    return redirect('SignIn')    