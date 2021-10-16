from django.test import TestCase
from django.contrib.auth.models import User
from .models import Employee
from django.contrib.auth import get_user_model
import datetime

class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        for i in range(5):
            Employee.objects.create(
                user=User.objects.create(username='user' + str(i), 
                first_name = 'test' + str(i), 
                last_name = 'guy' + str(i), 
                email='test' + str(i) + '@guy.com', 
                password='strong_p4ssw0rd_test'),
                dateofbirth = datetime.date(1990 + i, 2 + i, 3 + i))
    
    def testUserField(self):
        for i in range(5):
            employee = Employee.objects.get(id=i+1)
            user = User.objects.get(username='user' + str(i))
            self.assertEqual(employee.user, user)

    def testDateOfBirth(self):
        for i in range(5):
            employee = Employee.objects.get(id=i+1)
            dob = datetime.date(1990 + i, 2 + i, 3 + i)
            self.assertEqual(employee.dateofbirth, dob)
