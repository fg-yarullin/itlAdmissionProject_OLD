# Generated by Django 3.1.7 on 2021-06-03 23:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_tour', '0026_auto_20210601_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='touruploadfile',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first_tour.subject', verbose_name='Предмет'),
        ),
        migrations.AddField(
            model_name='touruploadfile',
            name='tour_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='touruploadfile',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first_tour.tour', verbose_name='Тур'),
        ),
        migrations.AlterField(
            model_name='userappeal',
            name='appeal_apply_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 3, 23, 17, 19, 730364), verbose_name='Время подачи заявления'),
        ),
    ]
