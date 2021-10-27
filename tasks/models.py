from django.db import models
from django.contrib.auth.models import User

from userprofile.models import Employee

class Task(models.Model):
    title = models.CharField(max_length=60)

    assigner = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)

    #Date task is created. By default should be now.
    date_created = models.DateTimeField(auto_now_add=True)
    
    date_completed = models.DateTimeField(null=True, blank=True)

    #Description of task. Can be empty.
    description = models.TextField(blank=True)

    is_complete = models.BooleanField(default=False)

    #The employee object who is assigned a task. Ultimately this should be a list
    # of employee objects since each task could be assigned to one or many employees.
    # By default this should be assigned to no employees. All employees should also be an option. 
    assignee = models.ManyToManyField(Employee, related_name='assignee')

    def __str__(self):
        return self.title