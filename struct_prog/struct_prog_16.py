# Написать программу, в которой вводятся два операнда
# Х и Y и знак операции sign (+, –, /, *).
# Вычислить результат Z в зависимости от знака.
# Предусмотреть реакции на возможный неверный знак операции,
# а также на ввод Y=0 при делении.
# Организовать возможность многократных вычислений
# без перезагрузки программа (т.е. построить бесконечный цикл).
# В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').

while True:
    x = int(input('x: '))
    y = int(input('y: '))
    sign = input('sign: ')

    if sign == '0':
        print('Good bye!')
        break
    elif sign not in ['+', '-', '*', '/']:
        print('Wrong input sign')
        continue
    elif sign == '/':
        if y == 0:
            print('Cannot divide by zero')
            continue
        z = x / y
    elif sign == '*':
        z = x * y
    elif sign == '+':
        z = x + y
    elif sign == '-':
        z = x - y
    print(f'{x} {sign} {y} = {z}')
