from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, Group

from .forms import CreateUserForm
from django.db import IntegrityError

def user_profile(request):
    return render(request, 'userprofile/profile.html', {'name': 'profile'})

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
    
    form = CreateUserForm()

    if request.method == 'GET':
        return render(request, 'userprofile/register.html', {'form': form})
    else:
       
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #username = form.cleaned_data.get('username')
            group = Group.objects.get(name='employees')
            user.groups.add(group)

            return redirect('profile:login')    
        else:
            #error
            return render(request, 'userprofile/register.html', 
            {'form': UserCreationForm(),
            'error':'Passwords did not match.'})

def logout_user(request):
    logout(request)
    return redirect('profile:login')

        
def other(request):
    return HttpResponse("Bad Page!")