# Generated by Django 4.2.4 on 2023-09-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_settings_admin_token_settings_telegram_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на видео'),
        ),
    ]
