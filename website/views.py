from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.db import IntegrityError


def homepage(request):
    return render(request, 'website/index.html', {'form': UserCreationForm(), 'name': 'home'})
        
#Page to signup new users. Eventually this should be for employees.
def signupuser(request):
    #check if going to page or submitting form
    if request.method == 'GET':
        return render(request, 'website/signupuser.html', {'form': UserCreationForm()})
    #user is trying to signup if a post is returned    

    else:
        if request.POST['password1'] == request.POST['password2']:
           
            #try to create new user if passwords match
            try:
                newuser = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                newuser.save()
                login(request, newuser)
                return redirect('homepage')
            except IntegrityError:
                return render(request, 'website/signupuser.html', 
                {'form': UserCreationForm(),
                'error':'Username is already taken.'})

                
        else:
            #error, passwords did not match
            return render(request, 'website/signupuser.html', 
            {'form': UserCreationForm(),
            'error':'Passwords did not match.'})
            

def other(request):
    return HttpResponse("Bad Page!")

def scheduling(request):
    return render(request, 'website/homepage.html', {'name': 'time_off'})

def payroll(request):
    return render(request, 'website/homepage.html', {'name': 'payroll'})

def payroll(request):
    return render(request, 'website/payroll.html')