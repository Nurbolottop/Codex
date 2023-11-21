# Generated by Django 4.2.7 on 2023-11-20 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide_image', verbose_name='Фотография для слайда')),
                ('title', models.CharField(max_length=255, verbose_name='Название для слайда')),
                ('descriptions', models.TextField(verbose_name='Описание для слайда')),
            ],
            options={
                'verbose_name': ('Слайд',),
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]