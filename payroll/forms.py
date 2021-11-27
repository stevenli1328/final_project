from django import forms
from django.forms import ModelForm
from userprofile.models import Employee
from django.forms import Select
from .models import Payroll

class PayrollForm(ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'pay_period_start', 'pay_period_end']

    employee = forms.ModelChoiceField(
        label = 'Select employee to view payroll data:',
        queryset=Employee.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    pay_period_start = forms.DateField(
        label = 'From date',
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    pay_period_end = forms.DateField(
        label = 'To date',
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

class PayrollViewForm(ModelForm):
    class Meta:
        model = Payroll
        fields = ['pay_period_start', 'pay_period_end']
    
    pay_period_start = forms.DateField(
        label = 'Get payroll data starting from:',
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    pay_period_end = forms.DateField(
        label = 'To date',
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )