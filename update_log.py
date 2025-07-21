from datetime import datetime, timezone

# Используем UTC для консистентности на серверах
now_utc = datetime.now(timezone.utc)
formatted_time = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")

try:
    # Открываем файл в режиме 'a' (append/добавление). 
    # Если файла нет, он будет создан.
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"Скрипт успешно выполнен: {formatted_time}\n")
    
    print("Файл log.txt успешно обновлен.")

except Exception as e:
    print(f"Произошла ошибка при записи в файл: {e}")