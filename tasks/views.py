from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group

from userprofile.models import Employee
from .forms import TaskForm, TaskEditForm, TaskViewForm
from .models import Task

import datetime


def manager_check(user):
    return user.groups.filter(name='managers')

@login_required(login_url='homepage')
def tasks(request):
    current_employee = None
    tasks = None
    managers = Group.objects.get(name='managers').user_set.all()
    employees = Group.objects.get(name='employees').user_set.all()

    if request.user in managers:
        current_employee = Employee.objects.get(user=request.user)
        tasks = Task.objects.order_by('-date_created')
    elif request.user in employees:
        current_employee = Employee.objects.get(user=request.user)
        tasks = current_employee.assignee.all().order_by('-date_due')
    return render(request, 'tasks/tasks.html', {'employee': current_employee, 'tasks': tasks})

@user_passes_test(manager_check, login_url='homepage')
def createtask(request):
    if request.method == 'GET':
        return render(request, 'tasks/newtask.html', {'form': TaskForm()})
    else:
        try:
            form = TaskForm(request.POST)
            newtask = form.save(commit=False)
            newtask.assigner = Employee.objects.get(user=request.user)
            newtask.save_m2m()
            newtask.save()
            return redirect('tasks:tasks')
        except ValueError:
            return render(request, 'tasks/newtask.html', {'form': form,'error': 'Please assign task to at least one person'})

@login_required(login_url='homepage')
def edittask(request, task_pk):
    task =  get_object_or_404(Task, pk=task_pk)
    if request.method == 'GET':
        if(manager_check(request.user)):
            form = TaskEditForm(initial={'date_due': task.date_due.date().isoformat()}, instance=task)
            return render(request, 'tasks/edittask.html', {'task':task, 'form': form})
        else:
            form = TaskViewForm(initial={'date_due': task.date_due.date().isoformat(), 'date_completed': datetime.date.today()}, instance=task)
            return render(request, 'tasks/edittask.html', {'task':task, 'form': form})
    else:
        try:
            form = TaskEditForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('tasks:tasks')
        except ValueError:
            return render(request, 'tasks/edittask.html', {'task':task, 'form': form, 'error': 'Bad information.'})

def deletetask(request, task_pk):
    task =  get_object_or_404(Task, pk=task_pk)
    if request.method=='POST':
        task.delete()
        return redirect('tasks:tasks')
    return render(request, 'tasks/deletetask.html', {'task': task})

def bad(request):
    return HttpResponse("Bad Page! Tasks")


# Create your views here.
