from django.forms import ModelForm
from django import forms
from .models import Schedule


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'employee', 'schedule_date', 'time_start', 'time_end']
    
    schedule_date = forms.DateField(widget=forms.SelectDateWidget)
#    time_start = forms.TimeField(widget=forms.TimeInput)

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'employee': forms.TextInput(attrs={'class': 'form-control'}),
        'schedule_date': forms.Select(attrs={'class': 'form-control'}),
        'time_start': forms.TextInput(attrs={'class': 'form-control'}),
        'time_end': forms.TextInput(attrs={'class': 'form-control'}),
    }