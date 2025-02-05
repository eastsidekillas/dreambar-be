import requests
from django.conf import settings


def send_to_telegram(name, phone, created_at):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    message = f"Бронирование стола:\nИмя: {name}\nТелефон: {phone}\nДата заявки: {created_at}"

    payload = {
        'chat_id': settings.TELEGRAM_CHAT_ID,  # ID чата или группы
        'text': message
    }

    # Отправка запроса на API Telegram
    response = requests.post(url, data=payload)

    # Логируем или проверяем успешность отправки
    if response.status_code != 200:
        print(f"Ошибка отправки в Telegram: {response.text}")
    else:
        print("Сообщение успешно отправлено в Telegram.")
