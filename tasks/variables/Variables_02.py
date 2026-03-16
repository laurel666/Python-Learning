"""
ЗАДАЧА: Variables_02

Описание:

Нужно посчитать итог по онлайн-заказу.
Дано:

- item_price = 1899.90
- quantity = 2
- discount_percent = 15
- delivery_price = 249

Нужно:

1. Посчитать стоимость товаров без скидки.
2. Посчитать размер скидки в деньгах.
3. Посчитать итоговую сумму с учётом скидки и доставки.
4. Вывести понятный чек в 3-4 строках.

Подсказки:

- процент удобно считать через деление на 100
- денежный вывод оформи через `{value:.2f}`
"""

# Напиши решение ниже.

item_price = 1899.90
quantity = 2
discount_percent = 15
delivery_price = 249

total_price = item_price * quantity
discount_amount = total_price * discount_percent / 100
final_price = total_price - discount_amount + delivery_price
print(f"Стоимость товаров без скидки: {total_price:.2f} руб.")
print(f"Размер скидки: {discount_amount:.2f} руб.")
print(f"Стоимость доставки: {delivery_price:.2f} руб.")
print(f"Итоговая сумма с учётом скидки и доставки: {final_price:.2f} руб.")