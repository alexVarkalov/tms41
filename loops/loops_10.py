# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы,
# которые кратны 3.

from random import randint

n = int(input('Enter n: '))

my_matrix = []

for i in range(n):
    line = []
    for j in range(n):
        line.append(randint(1, 10))
    my_matrix.append(line)

print(my_matrix)

my_summ = 0

for i in range(n):
    for j in range(n):
        if not my_matrix[i][j] % 3:
            my_summ += my_matrix[i][j]
print(my_summ)
