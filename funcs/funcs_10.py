# Рассчитать значение х определив и
# использовав необходимую функции. [02-5.1-BL01]


def calc_exception(n):
    result = (n ** 0.5 + n) / 2
    return result


def main():
    x = calc_exception(5) + calc_exception(12) + calc_exception(19)
    print(x)


if __name__ == '__main__':
    main()
