# Ввести с клавиатуры целое число n. Получить
# сумму кубов всех целых чисел от 1 до n(включая n)
# используя цикл while

n = int(input('Enter number '))
summ = 0
while n != 0:
    summ += n ** 3
    n -= 1
print(summ)
