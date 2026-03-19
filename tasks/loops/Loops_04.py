"""
ЗАДАЧА: Loops_04

Описание:

Есть список "сырых" тегов от пользователей:

raw_tags = ["  python ", "", " api", "data ", "  ", "backend"]

Нужно:

1. Пройтись циклом по списку.
2. Для каждого тега убрать лишние пробелы и привести к нижнему регистру.
3. Пустые теги не добавлять в результат.
4. Собрать новый список `clean_tags`.
5. Вывести `clean_tags`.

Подсказки:

- начни с `clean_tags = []`
- пустые значения удобно пропускать через `continue`
"""

# Напиши решение ниже.

raw_tags = ["  python ", "", " api", "data ", "  ", "backend"]
clean_tags = []

for tag in raw_tags:
    tag = tag.strip().lower()
    if not tag:
        continue
    clean_tags.append(tag)

print(clean_tags)