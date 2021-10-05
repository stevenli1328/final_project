from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm

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

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')

        
def other(request):
    return HttpResponse("Bad Page!")