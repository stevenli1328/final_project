# Generated by Django 3.2.7 on 2021-11-02 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_task_date_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_due',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 30, 5, 0, tzinfo=utc)),
        ),
    ]
