from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='homepage')
def viewtask(request, task_pk):
    task =  get_object_or_404(Task, pk=task_pk, assigner=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'tasks/viewtask.html', {'task':task, 'form': form})
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect(request, 'tasks:viewtask', task_pk=task.pk)
        except ValueError:
            return render(request, 'tasks/viewtask.html', {'task':task, 'form': form, 'error': 'Bad information.'})





def bad(request):
    return HttpResponse("Bad Page!")

# Create your views here.
