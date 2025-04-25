from django.db import models

# Create your models here.
from django. contrib. auth.models import AbstractUser

from Admin.models import Department,Location

class User(AbstractUser):
    usertype = models.CharField(max_length=50)    
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField(default=0) 

class User_Details(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)    
    # loc_id=models.ForeignKey(Location, on_delete=models.CASCADE)    
    address = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)

    
    

class Employee(models.Model):
    employee_id=models.ForeignKey(User, on_delete=models.CASCADE)  
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)     
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    salary=models.DecimalField(max_digits=8, decimal_places=2)

    experience=models.IntegerField() 
    rating=models.IntegerField(default=0)       