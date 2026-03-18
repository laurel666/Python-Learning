"""
ЗАДАЧА: Conditions_08

Описание:

Ты обрабатываешь статус заказа в интернет-магазине.

Дано:

- payment_status = "paid"
- stock_status = "out_of_stock"

Правила:

- если заказ оплачен и товар в наличии -> "Можно отправлять"
- если заказ оплачен, но товара нет -> "Ожидаем поступление"
- если заказ не оплачен -> "Ожидаем оплату"

Нужно:

1. Определить переменную `order_message`
2. Вывести строку:
   "Статус заказа: <message>"

Подсказки:

- здесь важно подумать о порядке условий
"""

# Напиши решение ниже.

payment_status = "paid"
stock_status = "out_of_stock"
order_message = "Ожидаем оплату"

if payment_status == "paid":
   if stock_status == "out_of_stock":
      order_message = "Ожидаем поступление"
   else:
      order_message = "Можно отправлять"

print(f"Статус заказа: {order_message}")