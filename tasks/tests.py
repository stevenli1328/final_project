from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from userprofile.models import Employee
import datetime


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        assigner1 = Employee.objects.create(
                user=User.objects.create(username='kurt'),
                dateofbirth=datetime.date(1988, 8, 18))

        task = Task.objects.create(
            title='do some things',
            assigner=assigner1,
            date_created=datetime.date(2021, 10, 16),
            description='a bunch of descriptors here'
        )

        task.assignee.add(assigner1)
    
    def test_the_task(self):
        task = Task.objects.get(id=1)
        employee = Employee.objects.get(id=1)
        self.assertEqual(task.assigner, employee)