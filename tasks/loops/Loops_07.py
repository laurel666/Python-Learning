"""
ЗАДАЧА: Loops_07

Описание:

Есть список тикетов поддержки:

tickets = ["Login issue", "Payment failed", "Profile not updating", "Email not received"]

Нужно:

1. С помощью `enumerate(..., start=1)` вывести тикеты с номерами.
2. Формат каждой строки:
   "<номер>. <текст тикета>"

Подсказки:

- здесь особенно удобно использовать `enumerate`
"""

# Напиши решение ниже.

tickets = ["Login issue", "Payment failed", "Profile not updating", "Email not received"]

for index, ticket in enumerate(tickets, start=1):
    print(index, ticket, sep=". ")