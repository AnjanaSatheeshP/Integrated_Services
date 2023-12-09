from django.db import models
from Home.models import Student
from Coordinator.models import Job
# Create your models here.



class Job_Application(models.Model):

    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,  default='Pending')
    apply_date=models.DateTimeField(auto_now_add=True, blank=True)