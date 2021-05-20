# Generated by Django 3.1.7 on 2021-05-20 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0026_auto_20210517_2332'),
        ('first_tour', '0013_auto_20210520_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userappeal',
            name='appeal_apply_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 18, 45, 33, 454252), verbose_name='Время подачи заявления'),
        ),
        migrations.AlterUniqueTogether(
            name='examresult',
            unique_together={('participant', 'exam_subject')},
        ),
        migrations.AlterUniqueTogether(
            name='tourparticipantscan',
            unique_together={('participant', 'tour')},
        ),
    ]
