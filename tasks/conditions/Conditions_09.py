"""
ЗАДАЧА: Conditions_09

Описание:

Ты проверяешь, можно ли применить промокод к заказу.

Дано:

- promo_code = " spring2026 "
- order_total = 4200
- is_first_order = False

Правила:

- если промокод после очистки равен `spring2026`
  и сумма заказа не меньше 4000, скидка применяется
- если это первый заказ и сумма заказа не меньше 2000, скидка тоже применяется
- иначе скидка не применяется

Нужно:

1. Нормализовать промокод
2. Определить переменную `discount_applied`
3. Вывести строку:
   "Скидка применена: <True/False>"

Подсказки:

- используй `strip()` и `lower()`
- здесь пригодится `or`
"""

# Напиши решение ниже.

promo_code = " spring2026 "
order_total = 4200
is_first_order = False
promo_code = promo_code.strip().lower()
discount_applied = (promo_code == "spring2026" and order_total >= 4000) or (is_first_order and order_total >= 2000)

print(f"Скидка применена: {discount_applied}")