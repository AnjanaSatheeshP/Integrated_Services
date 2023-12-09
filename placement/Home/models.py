from django.db import models

# Create your models here.
from django. contrib. auth.models import AbstractUser

from Admin.models import Department

class User(AbstractUser):
    usertype = models.CharField(max_length=50)     

class Student(models.Model):
    student_id=models.ForeignKey(User, on_delete=models.CASCADE)
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)    
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    father_name=models.CharField(max_length=30)    
    mother_name=models.CharField(max_length=30)    
    DOB=models.DateField()
    sslc=models.IntegerField()
    plus_two=models.IntegerField()    
    photo = models.FileField(
        upload_to='photo/')
    cv = models.FileField(
        upload_to='CV/')
    cgpa = models.FloatField()
    back_logs = models.IntegerField()
    
    

class Coordinator(models.Model):
    Coordinator_id=models.ForeignKey(User, on_delete=models.CASCADE)   
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    salary=models.IntegerField()
    experience=models.IntegerField()        