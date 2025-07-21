import os
import requests
import json
from dotenv import load_dotenv  # <--- ДОБАВЛЕНО: Импортируем функцию

load_dotenv()  # <--- ДОБАВЛЕНО: Загружаем переменные из файла .env в окружение

# --- НАСТРОЙКИ ---
# Ваш логин на GitHub
REPO_OWNER = 'instocky' 
# Название вашего репозитория
REPO_NAME = 'github-action'
# Имя файла воркфлоу, который нужно запустить
WORKFLOW_FILE_NAME = 'api-forward-workflow.yml' 

# Данные, которые мы хотим отправить в наш воркфлоу
INPUT_DATA = {
    "name": "Иннокентий",
    "email": "test@example.com",
    "message": "Это тестовый вызов из локального Python-скрипта!"
}
# -----------------

# Теперь os.getenv() сможет найти переменную, загруженную из .env файла
GITHUB_TOKEN = os.getenv('GITHUB_API_TOKEN')

# Проверяем, что токен задан
if not GITHUB_TOKEN:
    print("Ошибка: Переменная окружения GITHUB_API_TOKEN не найдена.")
    print("Убедитесь, что файл .env существует в корне проекта и содержит токен.")
    exit(1)

# ... остальная часть скрипта остается БЕЗ ИЗМЕНЕНИЙ ...

# Формируем URL для API-запроса
api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE_NAME}/dispatches"

# Формируем заголовки запроса
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

# Формируем тело запроса
payload = {
    "ref": "main",
    "inputs": INPUT_DATA
}

print(f"Отправка запроса на URL: {api_url}")
print(f"С данными: {json.dumps(INPUT_DATA, indent=2, ensure_ascii=False)}")

try:
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 204:
        print("\nУспех! Запрос на запуск воркфлоу принят GitHub.")
        print("Проверьте вкладку 'Actions' в вашем репозитории.")
    else:
        print(f"\nОшибка! GitHub API ответил со статусом: {response.status_code}")
        print(f"Тело ответа: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"\nПроизошла ошибка сети или запроса: {e}")