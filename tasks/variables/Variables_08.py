"""
ЗАДАЧА: Variables_08

Описание:

Нужно подготовить данные для логистического калькулятора.
Дано:

- length_cm = 40
- width_cm = 30
- height_cm = 20
- weight_kg = 6.5
- price_per_kg = 85

Нужно:

1. Посчитать объём коробки в кубических сантиметрах.
2. Посчитать стоимость доставки по весу.
3. Сформировать строку-отчёт с размерами, объёмом и стоимостью.

Подсказки:

- объём = длина * ширина * высота
- пока считаем стоимость только по весу, без условий
"""

# Напиши решение ниже.

length_cm = 40
width_cm = 30
height_cm = 20
weight_kg = 6.5
price_per_kg = 85

volume_cm3 = length_cm * width_cm * height_cm
weight_cost = weight_kg * price_per_kg
report = f"Dimensions: {length_cm} cm x {width_cm} cm x {height_cm} cm, Volume: {volume_cm3} cm3, Delivery Cost: {weight_cost}"

print(report)