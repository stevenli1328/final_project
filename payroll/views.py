from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

from datetime import datetime
from userprofile.models import Employee
from .models import Payroll
from .forms import PayrollForm


def payroll(request):
    employees = Employee.objects.all()

    
    if request.method=='POST':
        
        form = PayrollForm(request.POST or None)
        employee_name = form.data['employee']
        pay_period_start_date = datetime.strptime(form.data['pay_period_start'], '%Y-%m-%d').date()
        pay_period_end_date = datetime.strptime(form.data['pay_period_end'], '%Y-%m-%d').date()

        
        try:
            user = User.objects.get(username=employee_name)
        except User.DoesNotExist:
            return render(request, 'payroll/payroll.html', {'employees': employees, 'form': PayrollForm(), 'error': 'Please make a valid selection.'})
        
        employee = Employee.objects.get(user=user)
        if employee.payroll_set.first() != None:
            paystubs = employee.payroll_set.filter(pay_period_start__gte=pay_period_start_date,
            pay_period_end__lte=pay_period_end_date).order_by('-pay_period_end')

        else:
            return render(request, 'payroll/payroll.html', {'employees': employees, 'error': 'Employee has no payroll data'})
        return render(request, 'payroll/payrolldetail.html', {'paystubs': paystubs})

    else:
        payroll_form = PayrollForm()
        return render(request, 'payroll/payroll.html', {'employees': employees, 'form': payroll_form})

def viewpayroll(request):
    return render(request, 'payroll/payrolldetail.html', {'paystubs': paystubs})


def other(request):
    return HttpResponse("Bad Page! Payroll")