# Описать функцию Sin1( x , ε ) вещественного типа
# (параметры x , ε — вещественные, ε > 0),
# находящую приближенное значение функции sin( x ):
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ..
# .. + (–1)^n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε .
# С помощью Sin1 найти приближенное значение синуса для
# данного x при шести данных ε .  [01-11.3-Proc41]

from math import pi, sin


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sin1(x, e):
    sin_x = 0
    n = 0
    term = e
    while x > pi * 2:
        x -= pi * 2
    while abs(term) >= e:
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        sin_x += term
        n += 1
    return sin_x


def main():
    real = sin(pi / 6)
    res0001 = sin1(pi / 6 + pi * 0, 0.0001)
    res001 = sin1(pi / 6 + pi * 0, 0.001)
    res01 = sin1(pi / 6 + pi * 0, 0.05)
    print(real)
    print(res0001)
    print(res001)
    print(res01)
    print(sin1(pi / 6 + pi * 10 ** 6, 0.0001))
    print(sin1(3.14, 0.0001))


if __name__ == '__main__':
    main()
