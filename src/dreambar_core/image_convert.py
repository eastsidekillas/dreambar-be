from PIL import Image
import os
from django.core.files.base import ContentFile
from io import BytesIO


def convert_image_to_webp(image_field, upload_to):

    if not image_field:
        return None

    # Открываем изображение
    image = Image.open(image_field)
    image = image.convert("RGB")  # Конвертируем в RGB (WebP не поддерживает RGBA)

    # Генерируем новое имя файла
    filename = os.path.splitext(image_field.name)[0] + ".webp"

    # Создаём буфер для хранения изображения
    buffer = BytesIO()
    image.save(buffer, format="WebP", quality=80)  # Сохраняем в WebP с качеством 80%

    # Создаём файл Django
    return ContentFile(buffer.getvalue(), name=f"{upload_to}{filename}")
