from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from userprofile.models import Employee
import datetime, pytz

class TaskModelTest(TestCase):
    def setUp(self):
        manager = Employee.objects.create(
            user=User.objects.create(username='Manager')
        )
        employee1 = Employee.objects.create(
            user=User.objects.create(username='Employee1')
        )
        employee2 = Employee.objects.create(
            user=User.objects.create(username='Employee2')
        )

        pasttask = Task.objects.create(
            title='Here is a completed task in the past',
            description='',
            assigner=manager,
            date_due=datetime.date(2021, 8, 1),
            is_complete=True
        )   
        

        pasttask.assignee.add(employee1, employee2)
        

        oldtask = Task.objects.create(
            title='Here is a task in the past',
            description='Some text',
            assigner=manager,
            date_due=datetime.date(2021, 7, 15),
            is_complete=False
        )

        oldtask.assignee.add(manager)

        Task.objects.create(
            title='Here is a task in the present',
            description='Some text',
            assigner=manager,
            date_due=datetime.date.today(),
            is_complete=False        
        )

        futuretask = Task.objects.create(
            title='Here is a task in the future',
            description='Some text',
            assigner=manager,
            date_due=datetime.date(2021, 12, 30),
            is_complete=False
        )

        futuretask.assignee.add(employee1)


    def testTasksAssigner(self):
        pastCompletedTask = Task.objects.get(title='Here is a completed task in the past')
        pastNotCompletedTask = Task.objects.get(title='Here is a task in the past')
        presentTask = Task.objects.get(title='Here is a task in the present')
        futureTask = Task.objects.get(title='Here is a task in the future')
        manager = Employee.objects.get(id=1)

        self.assertEqual(pastCompletedTask.assigner, manager)
        self.assertEqual(pastNotCompletedTask.assigner, manager)
        self.assertEqual(presentTask.assigner, manager)
        self.assertEqual(futureTask.assigner, manager)

    def testTasksAssignee(self):
        pastCompletedTask = Task.objects.get(title='Here is a completed task in the past')
        pastNotCompletedTask = Task.objects.get(title='Here is a task in the past')
        presentTask = Task.objects.get(title='Here is a task in the present')
        futureTask = Task.objects.get(title='Here is a task in the future')
        pastassignees = pastCompletedTask.assignee.all()
        oldassignees = pastNotCompletedTask.assignee.all()
        presentassignees = presentTask.assignee.all()
        futureassignees = futureTask.assignee.all()
        

        self.assertQuerysetEqual(pastCompletedTask.assignee.all(), pastassignees,  ordered=False)
        self.assertQuerysetEqual(pastNotCompletedTask.assignee.all(),oldassignees,  ordered=False)
        self.assertQuerysetEqual(presentTask.assignee.all(), presentassignees,  ordered=False)
        self.assertQuerysetEqual(futureTask.assignee.all(), futureassignees,  ordered=False)

    def testTasksDate(self):
        pastCompletedTask = Task.objects.get(title='Here is a completed task in the past')
        pastNotCompletedTask = Task.objects.get(title='Here is a task in the past')
        presentTask = Task.objects.get(title='Here is a task in the present')
        futureTask = Task.objects.get(title='Here is a task in the future')
        now = datetime.datetime.now()
        now = pytz.utc.localize(now)

        self.assertLess(pastCompletedTask.date_due, now)
        self.assertLess(pastNotCompletedTask.date_due, now)
        self.assertLessEqual(presentTask.date_due, now)
        self.assertGreater(futureTask.date_due, now)