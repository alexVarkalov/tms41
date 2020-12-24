# Дана целочисленная квадратная матрица. Найти в
# каждой строке наибольший элемент и поменять
# его местами с элементом главной диагонали.
# [02-4.2-ML22]

from random import randint

matrix = []
n = int(input('--> '))
for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(-10, 10))
    matrix.append(row)

for row in matrix:
    print(row)
print()
for i, row in enumerate(matrix):
    max_elem = row[0]
    max_index = 0
    for j, elem in enumerate(row):
        if max_elem < elem:
            max_elem = elem
            max_index = j
    matrix[i][max_index] = matrix[i][i]
    matrix[i][i] = max_elem

for row in matrix:
    print(row)
