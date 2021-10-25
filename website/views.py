from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.db import IntegrityError

from tasks.models import Task




def homepage(request):
    tasks = Task.objects.order_by('-date_created')
    return render(request, 'website/managerdashboard.html', {'form': UserCreationForm(), 'tasks': tasks})

def other(request):
    return HttpResponse("Bad Page!")

def payroll(request):
    return render(request, 'website/main.html', {'name': 'payroll'})
