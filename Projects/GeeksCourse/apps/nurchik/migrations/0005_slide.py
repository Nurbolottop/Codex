# Generated by Django 4.2.6 on 2023-11-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurchik', '0004_alter_settings_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide_image/', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Введите название')),
                ('descriptions', models.TextField(verbose_name='Введите описание')),
            ],
        ),
    ]