from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group

from .forms import ScheduleForm, ScheduleEditForm, TimeOffRequestForm, TimeOffApproveForm
from .models import Schedule, TimeOffRequest
from userprofile.models import Employee
from tasks.models import Task
import datetime

import json
from django.core.serializers.json import DjangoJSONEncoder

def manager_check(user):
    return user.groups.filter(name='managers')

def employee_check(user):
    return user.groups.filter(name='managers') or user.groups.filter(name='employees')

@user_passes_test(employee_check, login_url='homepage')
def schedule(request):
    if(manager_check(request.user)):
        return render(request, 'schedule/schedule.html')
    else:
        return render(request, 'schedule/employeeschedule.html')

def eventsFeed(request):
    managers = Group.objects.get(name='managers').user_set.all()
    employees = Group.objects.get(name='employees').user_set.all()
    
    current_employee = Employee.objects.get(user=request.user)
    schedules = current_employee.schedule_set.all()
    if request.user in employees:
        tasks = current_employee.assignee.all()
        time_offs = current_employee.timeoffrequest_set.all()
    else:
        tasks = Task.objects.all()
        time_offs = TimeOffRequest.objects.all()
    json_list = []

    for schedule in schedules:
        title = schedule.title
        start = schedule.schedule_date.strftime("%Y-%m-%d") + 'T' + str(schedule.time_start)
        end = schedule.schedule_date.strftime("%Y-%m-%d") + 'T' + str(schedule.time_end)
        json_entry = {'title': title,'start': start, 'end': end}
        json_list.append(json_entry) 
        
    for time_off in time_offs:
        title = str(time_off.employee) + ': ' + time_off.title
        start = time_off.start_date.strftime("%Y-%m-%d")
        end = time_off.end_date.strftime("%Y-%m-%d")
        if(time_off.is_approved):
            color = 'green'
        else:
            color = 'red'
        json_entry = {'title': title,'start': start, 'end': end, 'color': color}
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
        task.date_due.date() - datetime.date.today() < datetime.timedelta(days=2)):
            color = 'yellow'
            textColor= 'black'
        
        json_entry = {'title': title, 'start': start, 'color': color, 'textColor': textColor, 'allDay': True}
        json_list.append(json_entry)
        
    return HttpResponse(json.dumps(json_list), content_type='application/json')

def createschedule(request):
    if request.method == 'GET':
        form = ScheduleForm(initial={'schedule_date': datetime.date.today()})
        return render(request, 'schedule/newschedule.html', {'form': form})
    else:
        try:
            form = ScheduleForm(request.POST)
            newschedule = form.save(commit=False)
            newschedule.save()
            return redirect('schedule:schedule')
        except ValueError:
            return render(request, 'schedule/newschedule.html', {'form': form,'error': 'Input Error'})

def editschedule(request, schedule_pk):
    schedule =  get_object_or_404(Schedule, pk=schedule_pk)
    if request.method == 'GET':
        form = ScheduleEditForm(initial={'schedule_date': schedule.schedule_date.isoformat()}, instance=schedule)
        return render(request, 'schedule/editschedule.html', {'schedule':schedule, 'form': form})
    else:
        try:
            form = ScheduleEditForm(request.POST, instance=schedule)
            if form.is_valid():
                form.save()
                return redirect('schedule:schedule')
        except ValueError:
            return render(request, 'schedule/editschedule.html', {'schedule':schedule, 'form': form, 'error': 'Bad information.'})

def deleteschedule(request, schedule_pk):
    schedule =  get_object_or_404(Schedule, pk=schedule_pk)
    if request.method=='POST':
        schedule.delete()
        return redirect('schedule:schedule')
    return render(request, 'schedule/deleteschedule.html', {'schedule': schedule})


def timeoffrequest(request):
    if request.method == 'GET':
        form = TimeOffRequestForm()
        return render(request, 'schedule/newtimeoff.html', {'form': form})
    else:
        try:
            form = TimeOffRequestForm(request.POST)
            form.save()
            return redirect('schedule:schedule')
        except ValueError:
            return render(request, 'schedule/newtimeoff.html', {'form': form, 'error': 'Input Error'})

def timeoff(request):
    timeoffrequests = TimeOffRequest.objects.order_by('-start_date')
    return render(request, 'schedule/viewtimeoff.html', {'timeoffrequests': timeoffrequests})

def approvetimeoff(request, timeoff_pk):
    timeoffrequest = get_object_or_404(TimeOffRequest, pk=timeoff_pk)
    
    if request.method == 'GET':
        form = form = TimeOffApproveForm(instance=timeoffrequest)
        return render(request, 'schedule/approvetimeoff.html', {'form': form})
    else:
        try:
            form = TimeOffApproveForm(request.POST, instance=timeoffrequest)
            if form.is_valid():
                form.save()
                return redirect('schedule:schedule')
        except ValueError:
            return render(request, 'schedule/approvetimeoff.html', {'form': form, 'error': 'Bad information.'})



def bad(request):
    return HttpResponse("Bad Page! Schedule")