# Generated by Django 4.2.6 on 2023-11-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurchik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='address',
            field=models.CharField(default=1, max_length=255, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='facebook',
            field=models.URLField(default=1, verbose_name='Ссылка на Facebook'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='instagram',
            field=models.URLField(default=1, verbose_name='Ссылка на инст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='logo',
            field=models.ImageField(default=1, upload_to='logo_image/', verbose_name='Логотип'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='phone',
            field=models.CharField(default=1, max_length=255, verbose_name='Номер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='youtube',
            field=models.URLField(default=1, verbose_name='Ссылка на ютуб'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='descriptions',
            field=models.TextField(verbose_name='Описание сайта'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название сайта'),
        ),
    ]