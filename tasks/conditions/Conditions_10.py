"""
ЗАДАЧА: Conditions_10

Описание:

Нужно определить приоритет заявки в службе поддержки.

Дано:

- client_plan = "business"
- issue_type = "payment"
- response_time_hours = 5

Правила:

- если тариф `business` и проблема связана с `payment`, приоритет `critical`
- если тариф `business` и время ответа больше 4 часов, приоритет `high`
- если тариф `pro` и время ответа больше 6 часов, приоритет `high`
- если время ответа больше 24 часов, приоритет `medium`
- иначе приоритет `normal`

Нужно:

1. Определить переменную `priority`
2. Вывести строку:
   "Priority: <priority>"

Подсказки:

- внимательно продумай порядок `if` / `elif`
- в таких задачах сначала ставят самые специфичные условия
"""

# Напиши решение ниже.

client_plan = "business"
issue_type = "payment"
response_time_hours = 5
priority = "normal"


if client_plan == "business" and issue_type == "payment":
   priority = "critical"
elif (client_plan == "business" and response_time_hours > 4) or (client_plan == "pro" and response_time_hours > 6):
   priority = "high"
elif response_time_hours > 24:
   priority = "medium"

print(f"Priority: {priority}")