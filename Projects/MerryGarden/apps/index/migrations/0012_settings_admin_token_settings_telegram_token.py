# Generated by Django 4.2.4 on 2023-09-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_settings_descriptions_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='admin_token',
            field=models.CharField(default=1, max_length=255, verbose_name='Админ айди'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='telegram_token',
            field=models.CharField(default=1, max_length=255, verbose_name='Телеграм токен'),
            preserve_default=False,
        ),
    ]