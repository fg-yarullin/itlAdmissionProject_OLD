# Generated by Django 3.1.7 on 2021-03-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0009_auto_20210307_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='portfolio_text',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Список дипломов?'),
        ),
    ]
