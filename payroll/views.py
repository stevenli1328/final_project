from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test

from datetime import datetime
from userprofile.models import Employee
from .models import Payroll
from .forms import PayrollForm, PayrollViewForm

def manager_check(user):
    return user.groups.filter(name='managers')

def payroll(request):    

    if request.method=='POST':
        if (not manager_check(request.user)):
            form = PayrollViewForm(request.POST or None)
            employee = Employee.objects.get(user=request.user)
            error = 'You have no payroll data for those dates.'
        else:
            form = PayrollForm(request.POST or None)
            employee = Employee.objects.get(id=form.data['employee'])
            error = 'That user has no payroll data.'

        pay_period_start_date = datetime.strptime(form.data['pay_period_start'], '%Y-%m-%d').date()
        pay_period_end_date = datetime.strptime(form.data['pay_period_end'], '%Y-%m-%d').date()
        if (pay_period_start_date >= pay_period_end_date):
            error = 'Please select valid dates.'
            return render(request, 'payroll/payroll.html', {'form': form, 'error': error})  
        paystubs = employee.payroll_set.filter(pay_period_start__gte=pay_period_start_date,
            pay_period_end__lte=pay_period_end_date).order_by('-pay_period_end')
        
        if not paystubs:
            error = "There doesn't seem to be payroll data for those dates."
            return render(request, 'payroll/payroll.html', {'form': form, 'error': error})  
        return render(request, 'payroll/payrolldetail.html', {'paystubs': paystubs, 'error': error})

    else:
        if(not manager_check(request.user)):
            payroll_form = PayrollViewForm()
        elif(manager_check(request.user)):
            payroll_form = PayrollForm()
        return render(request, 'payroll/payroll.html', {'form': payroll_form})


def viewpayroll(request):
    return HttpResponse("Bad Page! Payroll")

def other(request):
    return HttpResponse("Bad Page! Payroll")