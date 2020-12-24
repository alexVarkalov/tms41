# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]

from random import randint

n = 10
numbers = []
for i in range(n):
    numbers.append(randint(-10, 10))
print(numbers)

amount = 0
is_same = False
for i in range(1, n):
    if numbers[i] > numbers[i-1] and not is_same:
        amount += 1
        is_same = True
    else:
        is_same = False

print(amount)
