# Generated by Django 4.2.7 on 2023-11-08 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_normaladvert_options_alter_smalladvert_options'),
        ('all_categories', '0006_rename_secondblog_b2blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ThirdBlog',
            new_name='B3Blog',
        ),
    ]