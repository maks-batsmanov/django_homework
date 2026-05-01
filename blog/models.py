from django.db import models
from django.forms import CharField


class BlogEntry(models.Model):
    heading = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    publication_attribute = models.BooleanField(default=False, verbose_name='Признак публикации')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.heading
