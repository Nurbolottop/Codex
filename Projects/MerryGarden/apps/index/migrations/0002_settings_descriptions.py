# Generated by Django 4.2.4 on 2023-08-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='descriptions',
            field=models.TextField(default=1, verbose_name='Описание сайта'),
            preserve_default=False,
        ),
    ]
