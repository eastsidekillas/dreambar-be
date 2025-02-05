from django.db import models
from django.utils.text import slugify


class Event(models.Model):
    STATUS_CHOICES = [
        ('published', ('Опубликован')),
        ('moderation', ('На модерации')),
        ('archive', ('Архив')),
    ]

    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="Слаг", blank=True)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='events/', null=True, blank=True, verbose_name="Картинка")
    banner_image = models.ImageField(upload_to='events/banners/', null=True, blank=True, verbose_name="Баннерное изображение")
    event_date = models.DateTimeField(verbose_name="Дата и время мероприятия")
    content = models.TextField(verbose_name="Контент", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='moderation', verbose_name=('Статус'))

    def __str__(self):
        return self.title
