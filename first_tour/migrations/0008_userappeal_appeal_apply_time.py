# Generated by Django 3.1.7 on 2021-05-18 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_tour', '0007_tour_appeal_application_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userappeal',
            name='appeal_apply_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 18, 21, 50, 31, 197811), verbose_name='Время подачи заявления'),
        ),
    ]
