# Написать программу, которая будет выводить на экран
# случайные числа от 1 до 10 до тех пор, пока не выпадет 7.

from random import randint

counter = 0
while True:
    number = randint(1, 10)
    counter += 1
    if number == 7:
        break
    print(number)
print(f'{counter}')
