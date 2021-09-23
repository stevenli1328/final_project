from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request, 'website/homepage.html')
# Create your views here.

def other(request):
    return HttpResponse("Bad Page!")

def tasks(request):
    return HttpResponse("Tasks Page!")

def time_off(request):
    return HttpResponse('Time off')

def login(request):
    return HttpResponse('Login page')

def payroll(request):
    return HttpResponse('Payroll History')

