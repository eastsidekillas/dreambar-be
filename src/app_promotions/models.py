from django.db import models
from django.utils.text import slugify
from dreambar_core.image_convert import convert_image_to_webp


class Promotion(models.Model):

    STATUS_CHOICES = [
        ('published', ('Опубликован')),
        ('moderation', ('На модерации')),
        ('archive', ('Архив')),
    ]

    title = models.CharField(max_length=255, verbose_name="Название акции")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="Слаг", blank=True)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='promotions/', null=True, blank=True, verbose_name="Картинка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='moderation', verbose_name=('Статус'))

    def save(self, *args, **kwargs):
        if self.image:
            self.image = convert_image_to_webp(self.image, "")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
