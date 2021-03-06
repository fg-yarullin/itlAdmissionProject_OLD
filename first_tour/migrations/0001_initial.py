# Generated by Django 3.1.7 on 2021-05-17 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admission', '0026_auto_20210517_2332'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppealUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Полное имя предмета')),
                ('short_name', models.CharField(max_length=10, verbose_name='Короткое имя предмета')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название тура')),
                ('is_final_tour', models.BooleanField(default=False, verbose_name='Финальный тур?')),
                ('results_release_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата опубликования результатов')),
                ('tour_order', models.IntegerField(verbose_name='Какой по счету тур?')),
                ('parent_tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first_tour.tour', verbose_name='Предыдущий тур')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.CreateModel(
            name='ExamSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_scoring', models.CharField(choices=[('S', 'Балл'), ('R', 'Рекомендация'), ('Z', 'Зачет')], max_length=10, verbose_name='Тип оценивания')),
                ('max_score', models.IntegerField(verbose_name='Максимальный балл')),
                ('passing_score', models.IntegerField(verbose_name='Проходной балл')),
                ('ordering', models.IntegerField(default=100, verbose_name='Позиция в столбце')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_tour.subject', verbose_name='Предмет')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_tour.tour', verbose_name='Тур')),
            ],
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='Набранный балл')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='Комментарий')),
                ('appeal_application', models.CharField(blank=True, choices=[('N', 'Не заявился'), ('Z', 'Заявился')], max_length=10, null=True, verbose_name='Заявился на аппеляцию?')),
                ('appeal_reason', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Причина аппеляции')),
                ('is_absent_appeal', models.BooleanField(default=False, verbose_name='Отсутствовал на аппелляции')),
                ('appeal_time', models.DateTimeField(blank=True, null=True, verbose_name='Время аппелляции')),
                ('appeal_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first_tour.appealuser', verbose_name='Учителя аппеллирующий')),
                ('exam_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_tour.examsubject', verbose_name='Предмет')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.participant', verbose_name='Абитуриент')),
            ],
        ),
        migrations.AddField(
            model_name='appealuser',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_tour.tour', verbose_name='Тур'),
        ),
        migrations.AddField(
            model_name='appealuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
