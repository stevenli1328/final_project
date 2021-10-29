from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import datetime

from .forms import CreateUserForm
from userprofile.models import Employee
from django.db import IntegrityError

@login_required(login_url='homepage')
def user_profile(request, username):
    employee = Employee.objects.get(user=request.user)

    return render(request, 'userprofile/profile.html', {'employee': employee})

def login_user(request):
    if request.method == 'GET':
        return render(request, 'userprofile/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'userprofile/login.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match.'})
        else:
            login(request, user)
            return redirect('homepage')

#Page to signup new users. Eventually this should be for employees.
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'userprofile/register.html', {'form': CreateUserForm()})
    else:
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='employees')
            newemployee = Employee(user=user)
            newemployee.save()
            user.groups.add(group)
            login(request, user)
            return redirect('homepage')    
        else:
            #error
            messages.error(request, 'Bad shit')
            return render(request, 'userprofile/register.html', 
            {'form': CreateUserForm()})

def logout_user(request):
    logout(request)
    return redirect('profile:login')

        
def other(request):
    return HttpResponse("Bad Page!")