# Дано число. Найти сумму и произведение его цифр.

summ = 0
multi = 1
number = input('number: ')
if number.isdigit():
    for digit in number:
        int_digit = int(digit)
        summ += int_digit
        multi *= int_digit
print(f'sum is {summ}')
print(f'multi is {multi}')
