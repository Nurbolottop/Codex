# Generated by Django 4.2.7 on 2023-11-08 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_normaladvert_options_alter_smalladvert_options'),
        ('all_categories', '0010_rename_fivetwoblog_b6blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FiveThreeBlog',
            new_name='B7Blog',
        ),
    ]
