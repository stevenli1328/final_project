from django.contrib import admin
from .models import Payroll
from . import models

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created','assigner',)

admin.site.register(Payroll, TaskAdmin)
# Register your models here.
