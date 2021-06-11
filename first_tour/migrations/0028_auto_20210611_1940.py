# Generated by Django 3.1.7 on 2021-06-11 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_tour', '0027_auto_20210603_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='nexttourparticipantupload',
            name='type_of_pass',
            field=models.CharField(blank=True, choices=[('R', 'Резерв'), ('P', 'Прошел')], max_length=5, null=True, verbose_name='Тип прохождения'),
        ),
        migrations.AlterField(
            model_name='userappeal',
            name='appeal_apply_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 19, 40, 8, 105109), verbose_name='Время подачи заявления'),
        ),
    ]
