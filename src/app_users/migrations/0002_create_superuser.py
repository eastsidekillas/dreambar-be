from django.db import migrations
from django.conf import settings
from django.contrib.auth.hashers import make_password


def create_superuser(apps, schema_editor):
    # Получаем модель пользователя через apps.get_model
    User = apps.get_model(settings.AUTH_USER_MODEL.split('.')[0], settings.AUTH_USER_MODEL.split('.')[1])

    # Проверяем, есть ли суперпользователь
    if not User.objects.filter(is_superuser=True).exists():
        try:
            User.objects.create(
                email='admin@bardream.ru',
                is_staff=True,
                is_superuser=True,
                password=make_password('G1vWoTAYSd'),  # Используем make_password для хэширования
            )
        except Exception as e:
            raise RuntimeError(f"Не удалось создать суперпользователя: {e}")


class Migration(migrations.Migration):
    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
