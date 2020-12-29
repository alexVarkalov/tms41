# Создать функцию, которая принимает на вход неопределенное
# количество именованных аргументов и выводит на экран те из
# них, длина ключа которых четна.


def my_func(**kwargs):
    for key, value in kwargs.items():
        if not len(key) % 2:
            print(value)


def main():
    my_func(a=1, aa=2, aaa=3, aaaa=4)


if __name__ == '__main__':
    main()
