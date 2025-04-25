from django.db import models
from Home.models import User,User_Details
from Admin.models import Department,Location

# Create your models here.






   

class Job_Application(models.Model):
    user_id = models.ForeignKey(User,related_name='children_one', on_delete=models.CASCADE)
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)    
    work_details = models.CharField(max_length=130)
    work_date = models.DateField()
    employee_assigned_id=models.ForeignKey(User, related_name='children_two',on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=20,  default='Pending')
    apply_date=models.DateTimeField(auto_now_add=True, blank=True)
    status_updated = models.DateTimeField(null=True, blank=True)
    paid_amount=models.DecimalField(max_digits=8, decimal_places=2,null=True)
    comm_amount=models.DecimalField(max_digits=8, decimal_places=2,null=True)
    emp_amount=models.DecimalField(max_digits=8, decimal_places=2,null=True)
    is_feedback=models.BooleanField(default=0)
    is_rated=models.BooleanField(default=0)
    rating=models.IntegerField(default=0)
    feedback_details = models.CharField(max_length=230,null=True)
  
    

