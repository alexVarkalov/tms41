# В массиве целых чисел с количеством элементов 19
# определить максимальное число и заменить им все
# четные по значению элементы. [02-4.1-BL19]


from random import randint

number_list = []
for _ in range(19):
    number_list.append(randint(-10, 10))
print(number_list)

max_value = number_list[0]

for elem in number_list:
    if max_value < elem:
        max_value = elem

for i, elem in enumerate(number_list):
    if not elem % 2:
        number_list[i] = max_value

print(number_list)
