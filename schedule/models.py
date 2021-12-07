from django.db import models
from django.contrib.auth.models import User
from userprofile.models import Employee
from django.db.models import Q

from datetime import datetime

#schedule should be unique for a given employee for a given day.
class Schedule(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=['employee', 'schedule_date', 'title'], name='unique_shift')]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    schedule_date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        dateStr = str(self.employee) + ', ' + self.schedule_date.strftime("%d %b %Y") + ' ' + self.title
        return dateStr


class TimeOffRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        dateStr = str(self.employee) + ', ' + self.start_date.strftime("%d %b %Y") + ' to ' + self.end_date.strftime("%d %b %Y")
        return dateStr
