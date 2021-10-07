from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import TaskForm
from .models import Task


#Can this be better designed to not have to send empty dictionaries if the user is not logged in?
def tasks(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(assignee=request.user, date_completed__isnull=True)
    else:
        tasks = {}
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
            return redirect('tasks:tasks')
        except ValueError:
            return render(request, 'tasks/newtask.html', {'form': TaskForm(),'error': 'Input Error'})

def viewtask(request, task_pk):
    task =  get_object_or_404(Task, pk=task_pk)
    return render(request, 'tasks/viewtask.html', {'task':task})




def bad(request):
    return HttpResponse("Bad Page!")

# Create your views here.
