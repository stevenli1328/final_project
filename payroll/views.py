from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import PayrollForm
from .models import Tpayroll

# Can this be better designed to not have to send empty dictionaries if the user is not logged in?
def payroll(request):
    if request.user.is_authenticated:
        payroll = Payroll.objects.filter(assignee=request.user, date_completed__isnull=True)
    else:
        tasks = {}
    return render(request, 'payroll/payroll.html', {'name': 'payroll', 'payroll': tasks})

def createpayroll(request):
    if request.method == 'GET':
        return render(request, 'payroll/newpayroll.html', {'form': PayrollForm()})
    else:
        try:
            form = PayrollForm(request.POST)
            newpayroll = form.save(commit=False)
            newpayroll.assigner = request.user
            newpayroll.save()
            return redirect('payroll:payroll')
        except ValueError:
            return render(request, 'payroll/newpayroll.html', {'form': PayrollForm(),'error': 'Input Error'})

@login_required(login_url='homepage')
def viewtask(request, task_pk):
    task =  get_object_or_404(Task, pk=task_pk, assigner=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'payroll/viewpayroll.html', {'payroll':payroll, 'form': form})
    else:
        try:
            form = PayrollForm(request.POST, instance=task)
            form.save()
            return redirect(request, 'payroll:viewpayroll', payroll_pk=payroll.pk)
        except ValueError:
            return render(request, 'payroll/viewpayroll.html', {'payroll':payroll, 'form': form, 'error': 'Bad information.'})

def bad(request):
    return HttpResponse("Bad Page!")

# Create your views here.