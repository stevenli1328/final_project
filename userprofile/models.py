from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #extra features here
    first_name = models.CharField(max_length=15, default='')
    last_name = models.CharField(max_length=20, default='')
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    profile_picture = models.ImageField(default="default.png")

    #address
    street = models.CharField(max_length=200, null=True, blank=True, verbose_name='Street Address')
    city = models.CharField(max_length=75, null=True, blank=True, verbose_name='City')
    state = models.CharField(max_length=2, null=True, blank=True, verbose_name='State')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telephone Number')
    postal_code = models.CharField(max_length=5, null=True, blank=True, verbose_name='Postal Code')

    def __str__(self):
        return self.user.username

