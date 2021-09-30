from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task


def tasks(request):
    tasks = Task.objects.all()
    
    return render(request, 'tasks/tasks.html', {'name': 'tasks', 'tasks': tasks})

def createtask(request):
    if request.method == 'GET':
        return render(request, 'tasks/newtask.html', {'form': TaskForm()})
    else:
        try:
            form = TaskForm(request.POST)
            newtask = form.save(commit=False)
            newtask.assigner = request.user
            newtask.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks/newtask.html', {'form': TaskForm(),'error': 'Input Error'})



def bad(request):
    return HttpResponse("Bad Page!")

# Create your views here.
