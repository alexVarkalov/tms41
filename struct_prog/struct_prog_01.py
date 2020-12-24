# Ввести число с клавиатуры. Вернуть результат
# логического выражения: число больше 15 и число кратно 5.

number = float(input('Enter your number: '))
print(number > 15 and number % 5 == 0)
