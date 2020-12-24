# Дан двухмерный массив n × m элементов.
# Определить, сколько раз встречается
# число 7 среди элементов массива.[02-4.2-BL12]

from random import randint

n = int(input('n: '))
m = int(input('m: '))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(0, 9))
    matrix.append(row)

counter = 0


for row in matrix:
    print(row)
    for elem in row:
        if elem == 7:
            counter += 1
print(counter)
