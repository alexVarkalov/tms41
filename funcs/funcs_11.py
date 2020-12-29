# Написать функцию по решению квадратных уравнений.[b01-c11-Proc17]


def solve(a, b, c):
    """Calc quadratic equation"""
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
    # elif d == 0
    elif not d:  # not 0 -> not False -> True
        x1 = -b / (2 * a)
        x2 = x1
    else:
        print('No real roots')
        x1, x2 = 0, 0
    return x1, x2


def main():
    print(solve(4, -4, 1))
    print(solve(1, -1, -12))


if __name__ == '__main__':
    main()
