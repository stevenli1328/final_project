from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from userprofile.models import Employee
import datetime
import random

class TaskModelTest(TestCase):
    def setUp(self):
        manager = Employee.objects.create(
            user=User.objects.create(username='Mister_Manager')
        )
        employee1 = Employee.objects.create(
            user=User.objects.create(username='Employee1')
        )
        employee2 = Employee.objects.create(
            user=User.objects.create(username='Employee2')
        )

        Task.objects.create(
            title='Here is a completed task in the past',
            description='',
            assigner=manager,
            date_due=datetime.date(2021, 8, 1),
            is_complete=True
        )

        Task.objects.create(
            title='Here is a task in the past',
            description='Some text',
            assigner=manager,
            date_due=datetime.date(2021, 7, 15),
            is_complete=False
        )

        Task.objects.create(
            title='Here is a task in the present',
            description='Some text',
            assigner=manager,
            date_due=datetime.date.today(),
            is_complete=False        
        )

        Task.objects.create(
            title='Here is a task in the future',
            description='Some text',
            assigner=manager,
            date_due=datetime.date(2021, 12, 5),
            is_complete=False
        )


    def testReadTasks(self):
        pastCompletedTask = Task.objects.get(title='Here is a completed task in the past')
        pastNotCompletedTask = Task.objects.get(title='Here is a task in the past')
        presentTask = Task.objects.get(title='Here is a task in the present')
        futureTask = Task.objects.get(title='Here is a task in the future')
        user = User.objects.get(username='Mister_Manager')
        manager = Employee.objects.get(user=user)

        self.assertEqual(pastCompletedTask.assigner, manager)
        self.assertEqual(pastNotCompletedTask.assigner, manager)
        self.assertEqual(presentTask.assigner, manager)
        self.assertEqual(futureTask.assigner, manager)

    