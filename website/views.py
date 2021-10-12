from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.db import IntegrityError




def homepage(request):
    return render(request, 'website/main.html', {'form': UserCreationForm(), 'name': 'home'})

def other(request):
    return HttpResponse("Bad Page!")

def scheduling(request):
    return render(request, 'website/main.html', {'name': 'time_off'})

def payroll(request):
    return render(request, 'website/main.html', {'name': 'payroll'})

#def payroll(request):
#    return render(request, 'website/payroll.html')