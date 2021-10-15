from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=60)

    # Date task is created. By default should be now.
    date_created = models.DateTimeField(auto_now_add=True)
    
    date_completed = models.DateTimeField(null=True, blank=True)

    # Description of task. Can be empty.
    description = models.TextField(blank=True)

    # The employee object who is assigned a task. Ultimately this should be a list
    # of employee objects since each task could be assigned to one or many employees.
    # By default this should be assigned to no employees. All employees should also be an option. 
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignee')
    
    #The manager object who the task is assigned by. 
    assigner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigner', default=1)
