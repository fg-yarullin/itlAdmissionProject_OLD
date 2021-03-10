# Generated by Django 3.1.7 on 2021-03-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0006_auto_20210307_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='phone_party',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер телефона абитуриента'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='reg_status',
            field=models.IntegerField(default=3, verbose_name='Статус регистрации'),
        ),
    ]
