from django.db import models
from django.contrib.auth.models import User
from userprofile.models import Employee

from datetime import datetime


class Schedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        dateStr = self.schedule_date.strftime("%d %b %Y")
        return dateStr