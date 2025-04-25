from django.db import models
from django. contrib. auth.models import AbstractUser

# Create your models here.

class Department(models.Model):
    dept_name=models.CharField(max_length=30)
    
    
class Location(models.Model):
    loc_name=models.CharField(max_length=30)





