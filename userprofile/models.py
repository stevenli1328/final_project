from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #extra features here
    dateofbirth = models.DateField()

    def __str__(self):
        return self.user.name

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #extra features here
    dateofbirth = models.DateField()