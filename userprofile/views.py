from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import datetime

from .forms import CreateUserForm, EmployeeProfileForm
from userprofile.models import Employee
from django.db import IntegrityError

@login_required(login_url='/profile/login/')
def user_profile(request, username):
    employee = Employee.objects.get(user=request.user)
    form = EmployeeProfileForm(instance=employee)
    group = Group.objects.get(user=request.user)

    context = {'form': form, 
    'error': '', 
    'name': employee.first_name + " " + employee.last_name,
    'employee': employee,
    'group': group}
    

    if request.method=='GET':
        return render(request, 'userprofile/profile.html', context)
    else:
        form=EmployeeProfileForm(request.POST, request.FILES, instance=employee)
        context['form'] = form

        if form.is_valid:
            employee=form.save()
            return render(request, 'userprofile/profile.html', context)
        else:
            context['error'] = 'Some fields are invalid. Please try again.'
            return render(request, 'userprofile/profile.html', context)


def login_user(request):
    if request.method == 'GET':
        return render(request, 'userprofile/newlogin.html')
    else:
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user is None:
            return render(request, 'userprofile/newlogin.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match.'})
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
            messages.error(request, 'Bad info')
            return render(request, 'userprofile/register.html', 
            {'form': CreateUserForm()})

def logout_user(request):
    logout(request)
    return redirect('profile:login')

def editprofileinformation(request, username):
    employee = Employee.objects.get(user=request.user)
    form = EmployeeProfileForm(instance=employee)
    
    context = {'form': form, 
        'error': '', 
        'employee': employee}


    if request.method=='GET':
        return render(request, 'userprofile/editprofile.html', context)
    else:
        form=EmployeeProfileForm(request.POST, request.FILES, instance=employee)
        context['form'] = form

        if form.is_valid:
            employee=form.save()
            return redirect('profile:profile', username=request.user.username)
        else:
            context['error'] = 'Some fields are invalid. Please try again.'
            return render(request, 'userprofile/editprofile.html', context)



        
def other(request):
    return HttpResponse("Bad Page! Userprofile")