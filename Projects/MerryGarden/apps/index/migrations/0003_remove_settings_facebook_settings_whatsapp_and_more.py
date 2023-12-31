# Generated by Django 4.2.4 on 2023-08-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_settings_descriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='facebook',
        ),
        migrations.AddField(
            model_name='settings',
            name='whatsapp',
            field=models.URLField(blank=True, null=True, verbose_name='Whatspp URL'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram URL'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Youtube URL'),
        ),
    ]
