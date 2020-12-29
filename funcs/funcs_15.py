# Описать функцию fact2( n ),
# вычисляющую двойной факториал :n!! = 1·3·5·...·n,
# если n — нечетное; n!! = 2·4·6·...·n,
# если n — четное (n > 0 — параметр целого типа.
# С помощью этой функции найти двойные факториалы
# пяти данных целых чисел [01-11.2-Proc35]


def fact2(n):
    factorial = 1
    start = 2 if n % 2 == 0 else 3
    for i in range(start, n + 1, 2):
        factorial *= i
    return factorial


def main():
    print(fact2(5))
    print(fact2(6))


if __name__ == '__main__':
    main()
