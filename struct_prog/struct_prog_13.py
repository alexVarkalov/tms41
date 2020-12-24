# Дан словарь: {'test': 'test_value', 'europe': 'eur',
# 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
# получить список ключей - использовать метод .keys()

# (подсказка: создается новый ключ с цифрой в конце, старый
# удаляется)

# предоставить 2 решения. Одно с использованием цикла while,
# другое с использованием цикла for с параметром. Оба решения
# предоставить в одном файле.

while_my_dict = {
    'first': 'value one',
    'second': 'value two',
    'third': 'value three',
}

while_keys = list(while_my_dict.keys())
i = 0
while_keys_len = len(while_keys)
while i < while_keys_len:
    new_key = f'{while_keys[i]}{len(while_keys[i])}'
    while_my_dict[new_key] = while_my_dict.pop(while_keys[i])
    i += 1
print(while_my_dict)

for_my_dict = {
    'first': 'value one',
    'second': 'value two',
    'third': 'value three',
}

for_keys = list(for_my_dict.keys())
i = 0
for_keys_len = len(for_keys)
for i in range(for_keys_len):
    new_key = f'{for_keys[i]}{len(for_keys[i])}'
    for_my_dict[new_key] = for_my_dict.pop(for_keys[i])
print(for_my_dict)

for_my_dict = {
    'first': 'value one',
    'second': 'value two',
    'third': 'value three',
}

for_keys = list(for_my_dict.keys())
for old_key in for_keys:
    new_key = f'{old_key}{len(old_key)}'
    for_my_dict[new_key] = for_my_dict.pop(old_key)
print(for_my_dict)
