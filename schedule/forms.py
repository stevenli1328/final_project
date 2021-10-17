from django.forms import ModelForm
from .models import Schedule


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['employee', 'schedule_date', 'time_start', 'time_end']