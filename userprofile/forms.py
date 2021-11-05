from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from django.forms import SelectDateWidget


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmployeeProfileForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'date_of_birth', 'street','city', 'state', 'phone', 'profile_picture']
    
    date_of_birth = forms.DateField(widget=SelectDateWidget(years=range(1930,2010)))
