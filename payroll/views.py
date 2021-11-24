from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test

from datetime import datetime
from userprofile.models import Employee
from .models import Payroll
from .forms import PayrollForm, PayrollViewForm

def payroll(request):    
    managers = Group.objects.get(name='managers').user_set.all()
    employees = Group.objects.get(name='employees').user_set.all()

    if request.method=='POST':
        if request.user in employees:
            form = PayrollViewForm(request.POST or None)
            employee = Employee.objects.get(user=request.user)
            error = 'You have no payroll data for those dates.'
        else:
            form = PayrollForm(request.POST or None)
            employee_name = form.data['employee']
            try:
                user = User.objects.get(username=employee_name)
            except User.DoesNotExist:
                return render(request, 'payroll/payroll.html', {'form': PayrollForm(), 'error': 'Please make a valid selection.'})
            employee = Employee.objects.get(user=user)
            error = 'That user has no payroll data.'

        pay_period_start_date = datetime.strptime(form.data['pay_period_start'], '%Y-%m-%d').date()
        pay_period_end_date = datetime.strptime(form.data['pay_period_end'], '%Y-%m-%d').date()

        if employee.payroll_set.first() != None:
            paystubs = employee.payroll_set.filter(pay_period_start__gte=pay_period_start_date,
            pay_period_end__lte=pay_period_end_date).order_by('-pay_period_end')
        else:
            return render(request, 'payroll/payroll.html', {'form': form, 'error': error})
        return render(request, 'payroll/payrolldetail.html', {'paystubs': paystubs})

    else:
        if(request.user in employees):
            payroll_form = PayrollViewForm()
        elif(request.user in managers):
            payroll_form = PayrollForm()
        return render(request, 'payroll/payroll.html', {'form': payroll_form})


def viewpayroll(request):
    return HttpResponse("Bad Page! Payroll")

def other(request):
    return HttpResponse("Bad Page! Payroll")