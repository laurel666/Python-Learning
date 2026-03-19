"""
ЗАДАЧА: Loops_06

Описание:

У тебя есть времена ответа API в миллисекундах.
Некоторые значения отсутствуют и представлены как `None`:

response_times = [120, 98, None, 140, 110, None, 105]

Нужно:

1. Посчитать среднее время ответа только по числовым значениям.
2. Игнорировать `None`.
3. Сохранить результат в переменную `average_response_time`.
4. Вывести строку:
   "Среднее время ответа: <значение>"

Подсказки:

- понадобятся сумма и счётчик
- `None` удобно пропускать через `continue`
"""

# Напиши решение ниже.

response_times = [120, 98, None,  140, 110, None, 105]
count = 0
total_time = 0

for response_time in response_times:
    if response_time is None:
        continue
    count += 1
    total_time += response_time	

average_response_time = total_time / count

print(f"Среднее время ответа: {average_response_time}")