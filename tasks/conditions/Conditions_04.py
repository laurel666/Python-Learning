"""
ЗАДАЧА: Conditions_04

Описание:

Нужно определить статус скидки для клиента.

Дано:

- total_spent = 78000

Правила:

- если клиент потратил 100000 или больше -> "VIP"
- если клиент потратил 50000 или больше -> "Gold"
- если клиент потратил 10000 или больше -> "Silver"
- иначе -> "Basic"

Нужно:

1. Определить переменную `client_status`
2. Вывести строку:
   "Статус клиента: <status>"

Подсказки:

- здесь нужен `if` / `elif` / `else`
- проверяй условия от большего к меньшему
"""

# Напиши решение ниже.

total_spent = 78000
client_status = "Basic"

if total_spent >= 100000:
    client_status = "VIP"
elif total_spent >= 50000:
    client_status = "Gold"
elif total_spent >= 10000:
    client_status = "Silver"

print(f"Статус клиента: {client_status}")
