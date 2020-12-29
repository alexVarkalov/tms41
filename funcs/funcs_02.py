# Написать программу для работы с матрицами:
# ~ Создание
# ~ Вывод
# ~ Сумма всех элементов
# ~ Нахождение максимального элемента
# ~ Нахождение минимального элемента.
from random import randint

DEBUG = True


# Создать матрицу случайных чисел от a до b, размерность матрицы n*m
def create_matrix(n, m, a, b):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(randint(a, b))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def get_max_elem(matrix):
    max_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_elem:
                max_elem = elem
    return max_elem


def get_min_elem(matrix):
    min_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_elem:
                min_elem = elem
    return min_elem


def get_mutrix_sum(matrix):
    summ = 0
    for row in matrix:
        for elem in row:
            summ += elem
    return summ


def main():
    if DEBUG:
        n = 5
        m = 5
        a = 0
        b = 9
    else:
        n = input('Enter n: ')
        m = input('Enter n: ')
        a = input('Enter n: ')
        b = input('Enter n: ')

    matrix = create_matrix(n, m, a, b)
    print_matrix(matrix)
    print(get_mutrix_sum(matrix))
    print(get_max_elem(matrix))
    print(get_min_elem(matrix))


if __name__ == '__main__':
    main()
