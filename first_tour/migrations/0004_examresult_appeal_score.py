# Generated by Django 3.1.7 on 2021-05-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_tour', '0003_auto_20210518_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='examresult',
            name='appeal_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Аппелляционный балл'),
        ),
    ]
