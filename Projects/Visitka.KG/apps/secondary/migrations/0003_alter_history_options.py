# Generated by Django 4.2.7 on 2023-11-08 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0002_history_alter_team_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'Наша история', 'verbose_name_plural': 'Наши истории'},
        ),
    ]
