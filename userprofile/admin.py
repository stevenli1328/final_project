from django.contrib import admin
from .models import Employee, Manager


admin.site.register(Employee)
admin.site.register(Manager)