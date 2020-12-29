# Создать функцию, которая принимает на вход неопределенное
# количество аргументов и возвращает их сумму и максимальное из них.


def my_func(*args):
    summ = 0
    max_elem = args[0]
    for elem in args:
        summ += elem
        if max_elem < elem:
            max_elem = elem
    return summ, max_elem


def main():
    print(my_func(1, 2, 3, 4, 5, 6, 7, 8, 9))


if __name__ == '__main__':
    main()
