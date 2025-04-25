from django.shortcuts import render

from Admin.models import Department,Location
from Home.models import User_Details,User,Employee
from Customer.models import Job_Application
from django.http.response import HttpResponse

# Create your views here.
from datetime import datetime

from django.db.models import F, Q, Max
from django.db.models import Case, When, Value, CharField

def Customerhome(request):
    cust =request.session.get('customerid')    
        
    cust_id=User.objects.get(id=cust)

    fname=cust_id.first_name
    lname=cust_id.last_name
    name=fname+" "+lname

    return render(request,'customer/home.html' ,{'name':name})




def cust_apply_job(request):
    if request.method=="POST":
        print('.........................')
        cust =request.session.get('customerid')    
        
        cust_id=User.objects.get(id=cust)
        

        
        department=request.POST['dept_id']
        department_id = Department.objects.get(id=department)
        work_details=request.POST['work_details']
        work_date=request.POST['work_date']
        
      
        jop_apply=Job_Application.objects.create(user_id=cust_id,department_id=department_id,
                                                 work_details=work_details,work_date=work_date
                                 )
        jop_apply.save()
        
        return HttpResponse("<script>window.alert('Successfully Applied !!');window.location.href='/Customer/view_job_applications/'</script>")
    else:
        x=Department.objects.all()
        
        return render(request,'customer/add_Jobs.html',{'dept':x})     
    
def view_job_applications(request):  
    cust =request.session.get('customerid')    
        
    cust_id=User.objects.get(id=cust)
    
    result  = Job_Application.objects.filter(user_id_id=cust_id).select_related('department_id')
    result=Job_Application.objects.filter(user_id_id=cust_id).select_related('department_id').annotate(
    assined_status=Case(
        When(employee_assigned_id_id=1, then=Value('not assigned')),
        default=Value('Assigned'),
        output_field=CharField(),
    )
)
    print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,',result)
    return render(request,'customer/view_job_applications.html',{'result':result[::-1]})       


def del_apply_job_byUser(request,id):
    job=Job_Application.objects.get(id=id)
    job.delete()
    return HttpResponse("<script>window.alert('Successfully Deleted !!');window.location.href='/Customer/view_job_applications/'</script>")


def view_completed_jobs(request):
    cust =request.session.get('customerid')            
    cust_id=User.objects.get(id=cust)
    
    result=Job_Application.objects.filter(user_id_id=cust_id, status='Completed')
    result=Job_Application.objects.select_related('employee_assigned_id').filter(user_id_id=cust_id, status='Completed')
    
    return render(request,'customer/view_completed_jobs.html',{'result':result})



def feedback_rating_completed_jobs(request):  
   
        
    cust =request.session.get('customerid')            
    cust_id=User.objects.get(id=cust)
    result = Job_Application.objects.select_related('employee_assigned_id').filter(user_id_id=cust_id, status__in = ('Completed','Paid'))
    print(result)
    return render(request,'customer/view_jobs_feedback_rating.html',{'result':result}) 


def cust_feedback(request,id):
    if request.method=="POST":
        feedback=request.POST['feedback_details']
        
        
        data = Job_Application.objects.get(id=id)
        data.is_feedback=True
        data.feedback_details=feedback
        data.save()
        
       
        
        return HttpResponse("<script>window.alert('Feedback Send Successfully  !!');window.location.href='/Customer/feedback_rating_completed_jobs/'</script>")
    
    else:
        
   
        return render(request,'customer/feedback.html') 


def cust_rating(request,id):
    if request.method=="POST":
        rate=request.POST['rate']
        
        print(rate)
        data = Job_Application.objects.get(id=id)
        data.is_rated=True
        data.rating=rate
        data.save()
        
        empid=data.employee_assigned_id
        
        print(empid)
        
        emp=Employee.objects.get(employee_id=empid)
        
        emp.rating+=int(rate)
        sal= float( emp.salary)
        newsal=sal*(2/100)
        if int(rate)>=3:
            
            emp.salary=sal+newsal
        else:
            emp.salary=sal-newsal    
            
        emp.save()
        
        return HttpResponse("<script>window.alert('Successfully Rated !!');window.location.href='/Customer/feedback_rating_completed_jobs/'</script>")
    
    else:
        
   
        return render(request,'customer/rating.html') 
    
    



# -------------------payment------------------------------


    
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
  
def cust_pay(request,jid,eid): #id
    if id==0:
        client = razorpay.Client(auth =("rzp_test_ifqXZb84qSL1CP" , "IwSyyaBvXh300nlqM0kqb0ow"))
        payment = client.order.create({'amount':request.session['donation_id'], 'currency':'INR',
                                'payment_capture':'1' })
            # customerid = request.session['user_id']
        return render(request, 'customer/razorpay.html' ,{'payment':payment,"customerid":id})

    else:
        
        if request.method == "POST":
            print('//////////////')
            name = request.POST.get('name')
            # amount =int(request.POST.get('amount'))*100
            emp=Employee.objects.get(employee_id_id=eid)
            salary=float( emp.salary)
            print('salary ->',salary)
            
            commis=(salary*10)/100
            
            print('commis  ->>>>',commis)
            amountToPay=salary+commis
            print('amountToPay----->>>',amountToPay)
            amount = int(float(amountToPay))*100
            print(amount)
            email=request.POST.get('email')
            client = razorpay.Client(auth =("rzp_test_ifqXZb84qSL1CP" , "IwSyyaBvXh300nlqM0kqb0ow"))
            payment = client.order.create({'amount':amount, 'currency':'INR',
                                'payment_capture':'1' })
            # customerid = request.session['user_id']
            return render(request, 'customer/razorpay.html' ,{'payment':payment,"jobid":jid})
        else:
            customerid = request.session.get('customerid') 
            
            
            emp=Employee.objects.get(employee_id_id=eid)
            salary=float( emp.salary)
            print('salary ->',salary)
            
            commis=(salary*10)/100
            
            print('commis  ->>>>',commis)
            amountToPay=salary+commis
            print('amountToPay----->>>',amountToPay)
         
            userid= request.session.get('customerid') 
            return render(request, 'customer/razorpay.html',{"amountToPay":amountToPay,"jobid":jid,'user_id':userid} )



@csrf_exempt
def success(request,jid,amount):
    print(id,amount)
   
    if request.method == "POST":
        a = request.POST
        order_id = ""
       
        for key , val in a.items():
            
            if key == "razorpay_order_id":
                p_amount=amount/100
                print('p_amount--------->' , p_amount)
                e_amount=p_amount/(1+0.10)
                print('e_amount--------',e_amount)
                c_amount=p_amount-e_amount
                print('c_amount----',c_amount)
                order_id = val
             
                job=Job_Application.objects.get(id=jid)
                
                emp=job.employee_assigned_id
                employee=Employee.objects.get(employee_id_id=emp)
                
                job.paid_amount=amount/100
                job.status_updated=datetime.now()
                job.status="Paid"
                job.comm_amount=c_amount
                job.emp_amount=employee.salary
                job.save()
                
                break
     
    return render(request, "customer/success.html")


# ---------------------------paymenyt end 


def cust_editprofile(request):
    if request.method=="GET":
        cid=request.session.get('customerid') 
        user_de=User_Details.objects.get(user_id=cid)
        x=Location.objects.all()
        return render(request,'Customer/edit_profile.html',{'data':user_de,'loc':x})
    else:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        # salary=request.POST['salary']
        # experience=request.POST['experience']
        # username=request.POST['username']
        # password=request.POST['password']
        
        # loc=request.POST['loc_id']
        # loc_id = Location.objects.get(loc_name=loc) 
        
        cid=request.session.get('customerid')
        user_det=User_Details.objects.get(user_id=cid)
        
        user=User.objects.get(id=cid)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        # username=username,
        # password=password
        # ,usertype='Employee',
        user.address=address
        user.phone_number=phone
        user.save()
        
        # user_det.loc_id=loc_id
        user_det.address=address
        user_det.phone_number=phone
        
        user_det.save()
            
        return HttpResponse("<script>window.alert('Successfully Customer Profile Updated !!');window.location.href='/Customer/cust_editprofile/'</script>") 
    


def cust_set_loc(request):
    if request.method=="POST":
        cid=request.session.get('customerid') 
        user_de=User_Details.objects.get(user_id=cid)
        user_de.lat=request.POST['latitude']
        user_de.lng=request.POST['longitude']
        user_de.save()
        return HttpResponse("<script>window.alert('Successfully Location Updated !!');window.location.href='/Customer/cust_set_loc/'</script>") 
    else:
        
        cid=request.session.get('customerid') 
        user_de=User_Details.objects.get(user_id=cid)
        lat= user_de.lat
        lng=user_de.lng
        if lat=='' and lng=='':
            lat=8.5027295
            lng=76.9419737
            print('lat -->',lat ,'lng -->',lng )
            return render(request,'customer/set_loc.html',{'lat':lat,'lng':lng,'chk':0})  
        else:   
            return render(request,'customer/set_loc.html',{'lat':lat,'lng':lng,'chk':1})     
     