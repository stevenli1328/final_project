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



@login_required(login_url='/profile/login/')
def homepage(request):
    managers = Group.objects.get(name='managers').user_set.all()
    users = Group.objects.get(name='employees').user_set.all()
    

    if request.user in managers:
        tasks = Task.objects.order_by('-date_created')
        return render(request, 'website/managerdashboard.html', {'tasks': tasks, 'managers': managers, 'users': users})
    else:
        current_employee = Employee.objects.get(user=request.user)
        tasks = current_employee.assignee.all()
        return render(request, 'website/employeedashboard.html', {'tasks': tasks})


def employeeview(request):
    employees = Employee.objects.all()
    return render(request, 'website/employeeview.html',{'employees': employees})


def other(request):
    return HttpResponse("Bad Page!")


def payroll(request):
    return render(request, 'website/main.html', {'name': 'payroll'})