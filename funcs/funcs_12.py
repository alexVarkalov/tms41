# Описать функцию is_power_n( k , n ) логического типа, возвращающую
# True, если целый параметр k (> 0) является степенью числа n (> 1),
# и False в противном случае. Дано число n (> 1) и набор из 10 целых
# положительных чисел. С помощью функции is_power_n найти количество
# степеней числа n в данном наборе. [b01-c11-Proc27]


def is_power_n(k: int, n: int) -> bool:
    """
    Check if k is a power of n

    Parameters
    ----------
    k: int
        number
    n: int
        number

    Returns
    -------
    bool
        True if k is a power of n and False if not
    """
    while True:
        k /= n
        if k == 1:
            return True
        if k < 1:
            return False


def main():
    n = 2
    numbers = [25, 16, 81, 456, 42, 17, 8, 90, 100, 15]

    counter = 0
    for number in numbers:
        if is_power_n(number, n):
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()
