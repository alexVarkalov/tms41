# Просуммировать неопределенное количество чисел,
# вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп»

summ = 0
while True:
    number = input('Enter number: ')
    if number == 'stop':
        break
    summ += int(number)
print(f'sum = {summ}')
