# Generated by Django 3.1.7 on 2021-03-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0012_auto_20210312_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='have_profile',
            field=models.BooleanField(default=False, verbose_name='Есть профиль?'),
        ),
    ]
