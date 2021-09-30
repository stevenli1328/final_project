from django.shortcuts import render
from django.http import HttpResponse


def tasks(request):
    return render(request, 'tasks/tasks.html', {'name': 'tasks'})

def bad(request):
    return HttpResponse("Bad Page!")

# Create your views here.
