# Реализовать функцию возвращающую матрицу. На вход принимает
# n - размерность матрицы, random_from(по-умолчанию 1),
# random_to(по-умолчанию(9)).

from random import randint


def create_matrix(n, random_from=1, random_to=9):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(random_from, random_to))
        matrix.append(row)
    return matrix


def main():
    print(create_matrix(5))
    print(create_matrix(5, -9))
    print(create_matrix(5, -9, 19))


if __name__ == '__main__':
    main()
