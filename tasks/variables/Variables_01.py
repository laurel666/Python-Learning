"""
ЗАДАЧА: Variables_01

Описание:

Ты делаешь подготовку данных для карточки пользователя в CRM.
Есть отдельные переменные:

- first_name = "  анна "
- last_name = "иванова  "
- city = "  москва"
- birth_year = 2001
- current_year = 2026

Нужно:

1. Очистить строки от лишних пробелов.
2. Привести имя, фамилию и город к аккуратному виду.
3. Собрать переменную full_name.
4. Посчитать возраст.
5. Вывести строку:
   "Анна Иванова, 25 лет, г. Москва"

Подсказки:

- используй `strip()`
- используй `title()`
- для вывода используй `f-string`
"""

# Напиши решение ниже.
first_name = " анна "
last_name = "иванова  "
city = "  москва"
birth_year = 2001
current_year = 2026

first_name = first_name.strip().title()
last_name = last_name.strip().title()
city = city.strip().title()

full_name = f"{first_name} {last_name}"
age = current_year - birth_year
print(f"{full_name}, {age} лет, г. {city}")