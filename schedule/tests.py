from django.test import TestCase
from django.contrib.auth.models import User
from userprofile.models import Employee
import datetime

from .models import Schedule


class ScheduleModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        employee1 = Employee.objects.create(
                user=User.objects.create(username='kurt'),
                dateofbirth=datetime.date(1988, 8, 18))

        Schedule.objects.create(
            employee=employee1,
            schedule_date=datetime.date(2021, 10, 18),
            time_start=datetime.time(7,0,0),
            time_end=datetime.time(5,0,0), 
            date_created=datetime.date(2021, 10, 16)
        )
    
    def test_the_schedule(self):
        schedule = Schedule.objects.get(id=1)
        employee = Employee.objects.get(id=1)
        self.assertEqual(schedule.employee, employee)