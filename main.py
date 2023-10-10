import requests
import json

# URL сервера действий Rasa (замените на ваш реальный URL)
url = 'http://localhost:5055/webhook'

# JSON-запрос с данными для сервера действий
payload = {
    "next_action": "",  # Название действия, которое нужно выполнить
    "tracker": {
        "latest_message": {
            "text": "Пример сообщения от пользователя",
            "intent": {
                "name": "",  # Название намерения пользователя
                "confidence": 0.95  # Уверенность в намерении
            },
            "entities": [],  # Список сущностей, если есть
        },
        "slots": {},  # Слоты, если они нужны для действия
    },
}

# Отправка HTTP POST-запроса на сервер действий
response = requests.post(url, json=payload)

# Обработка ответа
if response.status_code == 200:
    # Ваш код для обработки успешного ответа сервера действий
    print(response.json())
else:
    # Обработка ошибки
    print(f"Ошибка {response.status_code}: {response.text}")