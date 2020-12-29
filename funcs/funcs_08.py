# Написать функцию принимающая на вход неопределенным количеством
# аргументов и именованный аргумент mean_type. В зависимости от
# mean_type вернуть среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.

def arithm_mean(*args):
    numbers_amount = len(args)
    summ = 0
    for number in args:
        summ += number
    mean = summ / numbers_amount
    return mean


def geom_mean(*args):
    numbers_amount = len(args)
    mult = 1
    for number in args:
        mult *= number
    g_mean = mult**(1/numbers_amount)
    return g_mean


def find_mean(mean_type, *args):
    if mean_type == 'arithm':
        return arithm_mean(*args)
    elif mean_type == 'geom':
        return geom_mean(*args)


def main():
    print('Geometrical mean:', find_mean('geom', 1, 2, 3, 4, 5, 6, 7, 8, 9))
    print('Arithmetical mean:', find_mean('arithm', 1, 2, 3, 4, 5, 6, 7, 8, 9))


if __name__ == '__main__':
    main()
