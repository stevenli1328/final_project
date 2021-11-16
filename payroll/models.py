from django.db import models
from userprofile.models import Employee

class Payroll(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=['employee', 'pay_period_end'], name='unique_pay_period') ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    is_paid = models.BooleanField(default=False)
