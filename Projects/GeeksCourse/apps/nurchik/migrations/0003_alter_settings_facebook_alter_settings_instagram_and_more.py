# Generated by Django 4.2.6 on 2023-11-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurchik', '0002_settings_address_settings_email_settings_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на Facebook'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на инст'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на ютуб'),
        ),
    ]
