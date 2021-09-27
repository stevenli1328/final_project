from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request, 'website/homepage.html')
# Create your views here.

def other(request):
    return HttpResponse("Bad Page!")

def tasks(request):
    return render(request, 'website/tasks.html')

def time_off(request):
    return render(request, 'website/scheduling.html')

def login(request):
    return render(request, 'website/login.html')

def payroll(request):
    return render(request, 'website/payroll.html')

