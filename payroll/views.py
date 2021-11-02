from django.shortcuts import render, redirect
from django.http import HttpResponse

from userprofile.models import Employee
from .models import Payroll


def payroll(request):
    employees = Employee.objects.all()

    if request.method=='POST':
        print(request.POST.get)
        #grab list of payroll objects associated with given employee
        #redirect to view page to see list of these objects
        return redirect('payroll:viewpayroll', payroll_id=1)
    else:
        return render(request, 'payroll/payroll.html', {'employees': employees})

def viewpayroll(request, payroll_id):
    paystub = Payroll.objects.get(payroll_id)

    return render(request, 'payroll/payrolldetail.html', {'paystub':paystub})


def other(request):
    return HttpResponse("Bad Page!")