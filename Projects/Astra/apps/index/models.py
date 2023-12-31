from django.db import models
from django_resized.forms import ResizedImageField
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип",
        blank = True, null = True
    )
    descriptions_contacts = models.TextField(
        verbose_name="Описание для страницы 'Контакты' ",
        blank=True,null=True
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефон номер',
        blank=True,null=True
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта',
        blank=True,null=True
        )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True,null=True
    )
    whatsapp = models.URLField(
        verbose_name='Whatspp URL',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram URL',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Youtube URL',
        blank=True, null=True
    )
    telegram_token = models.CharField(
        max_length=255,
        verbose_name="Телеграм токен",
        blank=True,null=True
    )
    admin_token = models.CharField(
        max_length=255,
        verbose_name="Админ айди",
        blank=True,null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Основная настройка"
            verbose_name_plural = "Основные настройки"