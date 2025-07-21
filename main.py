import datetime

# Получаем текущую дату и время
now = datetime.datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Привет от GitHub Actions! Скрипт запущен в: {formatted_time}")
print("Тестовый запуск прошел успешно!")