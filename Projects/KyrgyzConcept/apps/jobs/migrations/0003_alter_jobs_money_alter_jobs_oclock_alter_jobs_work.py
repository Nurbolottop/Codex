# Generated by Django 4.2.6 on 2023-10-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_jobs_money_jobs_oclock_jobs_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='money',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Зарплата'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='oclock',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Часы работы'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='work',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность'),
        ),
    ]