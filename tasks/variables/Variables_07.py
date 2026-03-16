"""
ЗАДАЧА: Variables_07

Описание:

Ты готовишь короткий чек для кофейни.
Дано:

- drink_name = "Cappuccino"
- drink_price = 240
- dessert_name = "Cheesecake"
- dessert_price = 320
- guest_name = "  maria "

Нужно:

1. Очистить имя гостя.
2. Посчитать итоговую сумму заказа.
3. Собрать многострочную строку чека.
4. Вывести чек в аккуратном виде.

Ожидается что-то близкое к:

Guest: Maria
Cappuccino: 240
Cheesecake: 320
Total: 560

Подсказки:

- используй `\n` или тройные кавычки
- имя приведи к виду `Maria`
"""

# Напиши решение ниже.

drink_name = "Cappuccino"
drink_price = 240
dessert_name = "Cheesecake"
dessert_price = 320
guest_name = "  maria ".strip().title()
total_sum = drink_price + dessert_price
receipt = f"""Guest: {guest_name}
{drink_name}: {drink_price}
{dessert_name}: {dessert_price}
Total: {total_sum}"""

print(receipt)