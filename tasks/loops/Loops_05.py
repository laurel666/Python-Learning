"""
ЗАДАЧА: Loops_05

Описание:

Есть список статусов счетов:

invoice_statuses = ["paid", "paid", "overdue", "paid", "pending"]

Нужно:

1. Найти первый счёт со статусом `overdue`.
2. Сохранить его позицию в переменную `first_overdue_index`.
3. Если просроченного счёта нет, сохранить `None`.
4. Вывести строку:
   "Первый просроченный счёт: <значение>"

Подсказки:

- используй `enumerate(..., start=1)`, чтобы получить человеческую нумерацию
- после нахождения первого подходящего элемента используй `break`
"""

# Напиши решение ниже.

invoce_statuses = ["paid", "paid", "overdue", "paid", "prnding"]
first_overdue_index = None

for index, status in enumerate(invoce_statuses, start=1):
    if status == "overdue":
        first_overdue_index = index
        break
    
print(f"Первый просроченный счёт: {first_overdue_index}")