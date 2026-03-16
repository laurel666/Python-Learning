"""
ЗАДАЧА: Variables_04

Описание:

Есть данные по диску сервера:

- disk_total_gb = 512
- disk_used_gb = 378.4

Нужно:

1. Посчитать свободное место.
2. Посчитать процент занятого места.
3. Посчитать процент свободного места.
4. Вывести строку:
   "Использовано: 378.40 GB (73.91%), свободно: 133.60 GB (26.09%)"

Подсказки:

- процент = часть / целое * 100
- форматируй числа до двух знаков после запятой
"""

# Напиши решение ниже.

disk_total_gb = 512
disk_used_gb = 378.4

disk_free_gb = disk_total_gb - disk_used_gb
percent_used = disk_used_gb / disk_total_gb * 100
percent_free = disk_free_gb / disk_total_gb * 100

print(f"Использовано: {disk_used_gb:.2f} GB ({percent_used:.2f}%), свободно: {disk_free_gb:.2f} GB ({percent_free:.2f}%)")