# Generated by Django 4.2.4 on 2023-09-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='founder', verbose_name='Фотография')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('found', models.CharField(max_length=255, verbose_name='Достижения')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Основатели',
                'verbose_name_plural': 'Основатель',
            },
        ),
    ]