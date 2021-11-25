from django.forms import ModelForm
from django import forms
from .models import Schedule, TimeOffRequest
from django.forms.widgets import NumberInput

from userprofile.models import Employee
import datetime

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['employee', 'title', 'schedule_date', 'time_start', 'time_end']
    
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Optional schedule title'}))

    schedule_date = forms.DateField(
        label = 'Schedule date:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    employee = forms.ModelChoiceField(
        label = 'Select employee to create shift for:',
        queryset=Employee.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    time_start = forms.TimeField(
        label = 'Start time:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'time'}
        )
    )

    time_end = forms.TimeField(
        label = 'End time:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'time'}
        )
    )

class TimeOffRequestForm(ModelForm):
    class Meta:
        model = TimeOffRequest
        fields = ['employee', 'title', 'start_date', 'end_date']

    title = forms.CharField(required=False, 
    label='Reason:',
     widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Reason for request'}))

    start_date = forms.DateField(
        label = 'Time off start:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    end_date = forms.DateField(
        label = 'Time off end:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    employee = forms.ModelChoiceField(
        label = 'Select employee to create request for:',
        queryset=Employee.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

class TimeOffApproveForm(ModelForm):
    class Meta:
        model = TimeOffRequest
        fields = ['employee', 'title', 'start_date', 'end_date', 'is_approved']

    title = forms.CharField(required=False,
    disabled=True, 
    label='Reason:',
     widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Reason for request'}))

    start_date = forms.DateField(
        disabled=True,
        label = 'Time off start:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    end_date = forms.DateField(
        disabled=True,
        label = 'Time off end:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    employee = forms.ModelChoiceField(
        disabled=True,
        label = 'Select employee to create request for:',
        queryset=Employee.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    is_approved = forms.BooleanField(required=False, 
    label='Approve this request', 
    widget=forms.CheckboxInput())


class ScheduleEditForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['employee', 'title', 'schedule_date', 'time_start', 'time_end']
    
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Optional schedule title'}))

    schedule_date = forms.DateField(
        label = 'Schedule date:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    employee = forms.CharField(
        disabled=True,
        label = 'Please create new schedule to change the employee',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    time_start = forms.TimeField(
        label = 'Start time:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'time'}
        )
    )

    time_end = forms.TimeField(
        label = 'End time:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'time'}
        )
    )