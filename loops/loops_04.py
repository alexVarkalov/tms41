# Просуммировать неопределенное количество чисел,
# вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп»
# не учитывать числа кратные 5

summ = 0
while True:
    number = input('Enter number: ')
    if number == 'stop':
        break
    if int(number) % 5 != 0:
        summ += int(number)
print(f'sum = {summ}')
