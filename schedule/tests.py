from django.test import TestCase
from django.contrib.auth.models import User
from userprofile.models import Employee
import datetime

from .models import Schedule


class ScheduleModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        employee1 = Employee.objects.create(
                user=User.objects.create(username='kurt'))

        Schedule.objects.create(
            employee=employee1,
            schedule_date=datetime.date(2021, 10, 18),
            time_start=datetime.time(7,0,0),
            time_end=datetime.time(5,0,0), 
            date_created=datetime.date(2021, 10, 16)
        )

        Schedule.objects.create(
            employee=employee1,
            schedule_date=datetime.date(2022, 10, 18),
            time_start=datetime.time(5,0,0),
            time_end=datetime.time(3,0,0), 
            date_created=datetime.date(2021, 10, 16)
        )
    
    def testemployee(self):
        schedule = Schedule.objects.get(id=1)
        employee = Employee.objects.get(id=1)
        self.assertEqual(schedule.employee, employee)

    def test_the_schedule(self):
        schedule1 = Schedule.objects.get(id=1)
        schedule2 = Schedule.objects.get(id=2)
        self.assertEqual(schedule1.schedule_date, datetime.date(2021, 10, 18))
        self.assertEqual(schedule2.schedule_date, datetime.date(2022, 10, 18))