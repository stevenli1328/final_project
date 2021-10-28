from django.forms import ModelForm
from .models import Payroll


class PayrollForm(ModelForm):
    class Meta:
        model = Task
        fields = ['Name', 'Date']