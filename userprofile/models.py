from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #extra features here
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=False)

    #address
    street = models.CharField(max_length=200, null=True, verbose_name='Street Address')
    city = models.CharField(max_length=75, null=True, verbose_name='City')
    state = models.CharField(max_length=2, null=True, verbose_name='City')
    phone = models.CharField(max_length=20, null=True, verbose_name='Telephone Number')
    postal_code = models.CharField(max_length=5, null=True, verbose_name='Postal Code')

    def __str__(self):
        return self.user.username
