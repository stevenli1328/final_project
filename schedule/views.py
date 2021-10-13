from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from userprofile.models import Employee


# Create your views here.
def schedule(request):
    current_employee = None
    schedules = None
    if request.user.is_authenticated:
        current_employee = Employee.objects.get(user=request.user)
        schedules = current_employee.schedule_set.all()
    return render(request, 'schedule/schedule.html', {'name': 'schedule', 'employee': current_employee, 'schedules': schedules})




def bad(request):
    return HttpResponse("Bad Page!")