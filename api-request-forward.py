import os
import requests
import json

# 1. Забираем данные из переменных окружения, которые установит GitHub Actions
user_name = os.getenv('INPUT_NAME', 'Имя не задано')
user_email = os.getenv('INPUT_EMAIL', 'Email не задан')
message = os.getenv('INPUT_MESSAGE', 'Сообщение не задано')

# 2. Указываем адрес, куда будем пересылать данные
webhook_url = 'https://webhook.site/9d3f3606-2219-4c7a-9f7b-bdee474a9bef'

# 3. Формируем тело запроса (payload) в виде словаря Python
payload = {
    'name': user_name,
    'email': user_email,
    'message': message,
    'source': 'Переслано через GitHub Actions'
}

print(f"Подготовлены данные для отправки: {json.dumps(payload, indent=2, ensure_ascii=False)}")
print(f"Отправка POST-запроса на адрес: {webhook_url}")

try:
    # 4. Отправляем POST-запрос с данными в формате JSON
    response = requests.post(webhook_url, json=payload)

    # 5. Проверяем результат и выводим в лог для отладки
    response.raise_for_status()  # Вызовет ошибку, если статус код 4xx или 5xx
    print("Запрос успешно отправлен!")
    print(f"Статус-код ответа: {response.status_code}")
    # Webhook.site часто возвращает тело ответа, его тоже можно вывести
    print(f"Тело ответа: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при отправке запроса: {e}")