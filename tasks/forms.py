from django.forms import ModelForm
from django import forms
from .models import Task
from django.forms.widgets import NumberInput

from userprofile.models import Employee


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'date_due']

    assignee = forms.ModelMultipleChoiceField(
        label = 'Assign To: ',
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'size': 8}))

    date_due = forms.DateField(
        label = 'Date Due:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder': 'Task title...'}))

    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
    'placeholder': 'Description...'}))

