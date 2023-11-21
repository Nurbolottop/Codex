from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo_image",
        verbose_name="Логотип"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    facebook = models.URLField(
        verbose_name="Ссылка от facebook"
    )
    instagram = models.URLField(
        verbose_name="Ссылка от instagram"
    )
    youtube = models.URLField(
        verbose_name="Ссылка от youtube"
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name="Основные параметры"
        verbose_name_plural="Основной параметр"