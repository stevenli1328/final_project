from django.forms import ModelForm
from django import forms
from .models import Task

from userprofile.models import Employee


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee']

    assignee = forms.ModelMultipleChoiceField(
    queryset=Employee.objects.all(),
    widget=forms.CheckboxSelectMultiple)
