from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError

from userprofile.models import Employee
from tasks.models import Task
from schedule.models import Schedule

import datetime


@login_required(login_url='/profile/login/')
def homepage(request):
    managers = Group.objects.get(name='managers').user_set.all()
    employees = Group.objects.get(name='employees').user_set.all()

    if request.user in managers or request.user.is_superuser:
        tasks = Task.objects.order_by('-date_created')[:10]
        schedules = Schedule.objects.filter(schedule_date=datetime.date.today())
        return render(request, 'website/managerdashboard.html', {'tasks': tasks, 'schedules': schedules, 'managers': managers, 'employees': employees})
    elif request.user in employees:
        current_employee = Employee.objects.get(user=request.user)
        tasks = current_employee.assignee.all().order_by('-date_due')
        return render(request, 'website/employeedashboard.html', {'tasks': tasks})
    else:
        return HttpResponse("Sorry, you aren't properly authenticated!")


def employeeview(request):
    managers = Group.objects.get(name='managers').user_set.all()
    employees = Employee.objects.all()

    return render(request, 'website/employeeview.html', {'employees': employees, 'managers': managers})
