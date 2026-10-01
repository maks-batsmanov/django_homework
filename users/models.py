from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text='Загрузите свой аватар')
    phone_number = models.CharField(max_length=20, blank=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=50, blank=True, help_text='Укажите страну')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
