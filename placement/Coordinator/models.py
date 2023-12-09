from django.db import models
from Admin.models import Department
# Create your models here.



class Job(models.Model):
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    no_of_vacancy = models.IntegerField()    
    cgpa = models.FloatField()    
    back_logs = models.IntegerField()
    last_date = models.DateField()
    package=models.FloatField()    
    bond=models.IntegerField()
    
    
class Resource(models.Model):
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    
    res = models.FileField(
        upload_to='res/')    
    topic = models.CharField(max_length=30)
    
        