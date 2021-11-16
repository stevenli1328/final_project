from django import forms
from django.forms import ModelForm
from userprofile.models import Employee
from django.forms import Select
from .models import Payroll

employee_list = []
employees = Employee.objects.all()
i = 1
for employee in employees:
    
    entry = [employee, str(employee)]
    entry_tuple = tuple(entry)
    employee_list.append(entry_tuple)
    i = i+1
choices = tuple(employee_list)

class PayrollForm(ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'pay_period_start', 'pay_period_end']

    employee = forms.CharField(
        label = 'Select Employee to view payroll data for:',
        widget=forms.Select(
            attrs={'class': 'form-control'}, 
            choices=(choices)
        )
    )

    pay_period_start = forms.DateField(
        label = 'From date',
        widget=forms.SelectDateWidget(
            years=[2021],
            attrs={'class': 'form-control'}
        )
    )

    pay_period_end = forms.DateField(
        label = 'To date',
        widget=forms.SelectDateWidget(
            years=[2021],
            attrs={'class': 'form-control'}
        )
    )