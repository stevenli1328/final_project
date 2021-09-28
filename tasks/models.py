from django.db import models

class Task(models.Model):
    title = models.CharField()
    date_created = models.DateTimeField()
    due_date = models.DateTimeField()
    description = models.TextField()
    #Employee Object
    #Manager Object

    
# Create your models here.
