from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created','assigner',)

admin.site.register(Task, TaskAdmin)
# Register your models here.
