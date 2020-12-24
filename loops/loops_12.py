# Дана целочисленная матрица А[n,m].
# Посчитать количество элементов матрицы,
# превосходящих среднее арифметическое значение
# элементов матрицы и сумма индексов которых четна.[02-4.2-BL23]

from random import randint

n = int(input('n: '))
m = int(input('m: '))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(0, 9))
    matrix.append(row)
summ = 0
for row in matrix:
    for elem in row:
        summ += elem

mean = summ / (n * m)
print(mean)

counter = 0
for i, row in enumerate(matrix):
    print(row)
    for j, elem in enumerate(row):
        if elem > mean and (i + j) % 2 == 0:
            counter += 1
print(counter)
