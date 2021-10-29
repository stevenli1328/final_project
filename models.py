from django.db import models
from django.contrib.auth.models import User

class Payroll(models.Model):

    title = models.CharField(max_length=60)

    # Date task is created. By default should be now.
    date_created = models.DateTimeField(auto_now_add=True)
    
    date_completed = models.DateTimeField(null=True, blank=True)

    # Description of task. Can be empty.
    description = models.TextField(blank=True)

    employee_timeoff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_timeoff')
    
    # the employee who is requesting time off
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Employee', default=1)