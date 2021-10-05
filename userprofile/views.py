from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout

def user_profile(request):
    return render(request, 'userprofile/profile.html', {'name': 'profile'})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
        
def other(request):
    return HttpResponse("Bad Page!")