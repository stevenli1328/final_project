from django.shortcuts import render, HttpResponse

def user_profile(request):
    return render(request, 'website/dashboard.html', {'name': 'profile'})

def other(request):
    return HttpResponse("Bad Page!")