from django.db import models
from userprofile.models import Employee
import datetime

class Payroll(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=['employee', 'pay_period_end'], name='unique_pay_period') ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        if self.is_paid:
            paid = 'Paid.'
        else:
            paid = 'Not paid.'
        return str(self.employee).capitalize() + ', ' + self.pay_period_end.strftime("%m/%d/%Y") + ', ' + paid