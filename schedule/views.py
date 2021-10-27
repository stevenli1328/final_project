from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import ScheduleForm
from userprofile.models import Employee

import json

# Create your views here.
def schedule(request):
    current_employee = None
    schedules = None

    events = [{ 'title': 'title',
                'start': '2020-10-30',
                'end': '2020-10-31'}]
    json_data = json.dumps(events)

    if request.user.is_authenticated:
        current_employee = Employee.objects.get(user=request.user)
        schedules = current_employee.schedule_set.all()
    
    return render(request, 'schedule/schedule.html', 
    {'name': 'schedule', 
    'employee': current_employee, 
    'schedules': schedules,
    'json_events': json_data})

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
    return HttpResponse("Bad Page!")