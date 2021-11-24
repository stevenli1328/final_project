from django.forms import ModelForm
from django import forms
from .models import Task
from django.forms.widgets import NumberInput
from django.contrib.auth.models import Group

from userprofile.models import Employee


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'team', 'date_due']

    assignee = forms.ModelMultipleChoiceField(
        label = 'Assign To: ',
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'size': 8}))

    team = forms.ModelMultipleChoiceField(
        required=False,
        label = 'Assign to team: ',
        queryset=Group.objects.all(),
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

    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
    'placeholder': 'Description...'}))


class TaskEditForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'team', 'date_due', 'is_complete', 'date_completed']

    assignee = forms.ModelMultipleChoiceField(
        label = 'Assign To: ',
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'size': 8}))

    team = forms.ModelMultipleChoiceField(
        required=False,
        label = 'Assign to team: ',
        queryset=Group.objects.all(),
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

    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
    'placeholder': 'Description...'}))

    is_complete = forms.BooleanField(required=False, label='Task Completed: ', widget=forms.CheckboxInput())

    date_completed = forms.DateField(
        required=False,
        label = 'Date completed:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

class TaskViewForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'team', 'date_due', 'is_complete', 'date_completed']

    assignee = forms.ModelMultipleChoiceField(
        disabled=True,
        label = 'Assign To: ',
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'size': 8}))

    team = forms.ModelMultipleChoiceField(
        disabled=True,
        label = 'Assign to team: ',
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'size': 8}))


    date_due = forms.DateField(
        disabled=True,
        label = 'Date Due:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )

    title = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder': 'Task title...'}))

    description = forms.CharField(disabled=True, widget=forms.Textarea(attrs={'class': 'form-control',
    'placeholder': 'Description...'}))

    is_complete = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    date_completed = forms.DateField(
        label = 'Date Due:',
        widget=NumberInput(
            attrs={'class': 'form-control',
            'type': 'date'}
        )
    )
