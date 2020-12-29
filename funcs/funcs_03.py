# Написать программу для нахождения факториала.
# Факториал натурального числа n определяется
# как произведение всех натуральных чисел от
# 1 до n включительно


def my_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def main():
    print(my_factorial(1))
    print(my_factorial(2))
    print(my_factorial(3))
    print(my_factorial(4))
    print(my_factorial(5))
    print(my_factorial(6))
    print(my_factorial(7))


if __name__ == '__main__':
    main()
