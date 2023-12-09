from django.db import models
from django. contrib. auth.models import AbstractUser

# Create your models here.

class Department(models.Model):
    dept_name=models.CharField(max_length=30)


    
class Courses(models.Model):
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30)


