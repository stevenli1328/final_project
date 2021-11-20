from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import ScheduleForm
from userprofile.models import Employee
from tasks.models import Task
import datetime

import json
from django.core.serializers.json import DjangoJSONEncoder


def employee_check(user):
    return user.groups.filter(name='managers') or user.groups.filter(name='employees')

@user_passes_test(employee_check, login_url='homepage')
def schedule(request):
    current_employee = None
    schedules = None

    if request.user.is_authenticated:
        current_employee = Employee.objects.get(user=request.user)
        schedules = current_employee.schedule_set.all()

    return render(request, 'schedule/schedule.html', 
    {'name': 'schedule', 
    'employee': current_employee, 
    'schedules': schedules})

def eventsFeed(request):
    current_employee = Employee.objects.get(user=request.user)
    schedules = current_employee.schedule_set.all()
    tasks = current_employee.task_set.all()
    json_list = []
    for schedule in schedules:
        title = schedule.title
        start = schedule.schedule_date.strftime("%Y-%m-%d") + 'T' + str(schedule.time_start)
        end = str(schedule.time_end)
        json_entry = {'title': title,'start': start, 'end': end}
        json_list.append(json_entry) 
    for task in tasks:
        title = task.title
        start = task.date_due.strftime("%Y-%m-%d")
        textColor = None
        color = None

        if(task.is_complete):
            color = 'green'
        elif(task.is_complete is not True and task.date_due.date() < datetime.date.today()):
            color = 'red'
        elif(task.is_complete is not True and 
        task.date_due.date() >= datetime.date.today() and 
        task.date_due.date() - datetime.date.today() < datetime.timedelta(hours=24)):
            color = 'yellow'
            textColor= 'black'
        
        json_entry = {'title': title, 'start': start, 'color': color, 'textColor': textColor, 'allDay': True}
        json_list.append(json_entry)
        
    return HttpResponse(json.dumps(json_list), content_type='application/json')

def createschedule(request):
        if request.method == 'GET':
            return render(request, 'schedule/newschedule.html', {'form': ScheduleForm()})
        else:
            try:
                form = ScheduleForm(request.POST)
                newschedule = form.save(commit=False)
                newschedule.save()
                return redirect('schedule:schedule')
            except ValueError:
                return render(request, 'schedule/newschedule.html', {'form': ScheduleForm(),'error': 'Input Error'})



def bad(request):
    return HttpResponse("Bad Page! Schedule")