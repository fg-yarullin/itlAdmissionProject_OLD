# Generated by Django 3.1.7 on 2021-03-06 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='Профиль обучения',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Профиль обучения',
        ),
        migrations.AddField(
            model_name='grade',
            name='profile_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='admission.profile', verbose_name='Профиль обучения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='1', max_length=100, verbose_name='Профиль обучения'),
            preserve_default=False,
        ),
    ]