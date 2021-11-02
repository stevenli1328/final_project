from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from userprofile.models import Employee
import datetime
import random

class TaskModelTest(TestCase):

    #Create 1 assigner employee and 10 new employees. 
    #Then create ten tasks, each with the same assigner, but each 
    #with some random number (between 1 and ten) of assignee's.
    @classmethod
    def setUpTestData(self):
        assigner1 = Employee.objects.create(
                user=User.objects.create(username='kurt'))

        employees = []

        for i in range(10):
            employees.append(Employee.objects.create(
                user=User.objects.create(username='employee number ' + str(i))
            ))


        for i in range(10):
            task = Task.objects.create(
                title='do thing number ' + str(i),
                assigner=assigner1,
                description='a bunch of descriptors here'
            )

            ass_count = random.randrange(10)
            print(ass_count)
            
            for j in range(ass_count):
                task.assignee.add(employees[j]) 


        