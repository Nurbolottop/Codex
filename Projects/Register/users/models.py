from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер",
        blank=True,null=True
    )
    def __str__(self):
        return self.email 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Blog(models.Model):
    pass

class SportBlog(models.Model):
    pass

class BussnuiseBlog(models.Model):
    pass