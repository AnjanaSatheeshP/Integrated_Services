from django.shortcuts import  render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from Admin.models import Department #,Location
from Home.models import User,User_Details,Employee



def home(request):   
    return render(request,'Home/home.html')
def about(request):   
    return render(request,'Home/about.html')
def contact(request):   
    return render(request,'Home/contact.html')

def admin_signIn(request):
    if request.method=="GET":
        context = {}
        context['form'] = ''
        return render(request,'Home/Admin_SignIn.html',context)

    elif request.method == 'POST':
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
      
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("adminhome")
            else:
                
                return HttpResponse("<script>window.alert('Invalid Admin Credentials!');window.location.href='/admin_signIn/'</script>")
               
        else:
            
            return HttpResponse("<script>window.alert('Invalid Credentials  !');window.location.href='/admin_signIn/'</script>")
        
def Emp_SignIn(request):
    if request.method=="GET":
        context = {}
        context['form'] = ''
        return render(request,'Home/Emp_SignIn.html',context)
    elif request.method == 'POST':
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
      
        if user is not None:
            login(request,user)
            if user.usertype == "Employee": # Employee
                login(request,user)
                request.session['Employee_id']=user.id 
                
                return redirect("Employeehome")
            else:
                
                return HttpResponse("<script>window.alert('Invalid Employee Credentials!');window.location.href='/Emp_SignIn/'</script>")
               
        else:
            
            return HttpResponse("<script>window.alert('Invalid Credentials  !');window.location.href='/Emp_SignIn/'</script>")
            
            
            

def User_SignIn(request):
    if request.method=="GET":
        context = {}
        context['form'] = ''
        return render(request,'Home/User_SignIn.html',context)

    elif request.method == 'POST':
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
      
        if user is not None:
            login(request,user)
            if user.usertype == 'customer': # student
                request.session["customerid"]=user.id
                
                return redirect("Customerhome")
            else:
                
                return HttpResponse("<script>window.alert('Invalid Customer Credentials!');window.location.href='/User_SignIn/'</script>")
               
        else:
            
            return HttpResponse("<script>window.alert('Invalid Credentials  !');window.location.href='/User_SignIn/'</script>")
            
       


def SignIn(request):
    print('...................')
    if request.method == 'GET':
        context = {}
        context['form'] = ''
        return render(request,'Home/SignIn.html',context)
    elif request.method == 'POST':
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
      
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("adminhome")
            else:
                if user.usertype == 'customer': # student
                    request.session["customerid"]=user.id
                    
                    return redirect("Customerhome")
                elif user.usertype == "Employee": # Employee
                        login(request,user)
                        request.session['Employee_id']=user.id 
                        
                        return redirect("Employeehome")
                else:
                    print('................')
                    return HttpResponse("<script>window.alert('INvalid!');window.location.href='/SignIn/'</script>")
               
        else:
            context = {}
            context['error'] = 'Invalid User or Admin not approved'
            return HttpResponse("<script>window.alert('INvalid!');window.location.href='/SignIn/'</script>")
        
   
    return HttpResponse("<script>window.alert('Invalid!');window.location.href='/SignIn/'</script>")


def user_reg(request):
  
    if request.method=="GET":
        
        return render(request,'Home/reg_Student.html')      
    else:
       
        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']     
        # loc=request.POST['loc_id']    
        # loc_id=Location.objects.get(id=loc) 
       
        username=request.POST['username']
        password=request.POST['password']
        
        if  User.objects.filter(username=username).exists():
            return HttpResponse("<script>window.alert('Username alredy Exist!!');window.location.href='/user_reg/'</script>")
            
        else:
        
            new_user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,
                                            password=password,usertype='customer',address=address,phone_number=phone)
            new_user.save()
            
            user_details=User_Details.objects.create(user_id=new_user,
                                        address=address,phone_number=phone
                                        ) #,loc_id=loc_id
            user_details.save()


            return HttpResponse("<script>window.alert('Successfully Customer Registered!!');window.location.href='/user_reg/'</script>")


def A_SignIn(request):
    print('...................')
    if request.method == 'GET':
        context = {}
        context['form'] = ''
        return render(request,'Home/SignIn.html',context)
  
   
   



def accounts_logout(request):
    logout(request)
    return redirect('home')    