# Дан список чисел. Посчитать сколько раз
# встречается каждое число. Использовать функцию.
# Подсказка: для хранения данных использовать
# словарь. Для проверки нахождения элемента в
# словаре использовать метод get(), либо оператор in


def calc_repetition(numbers):
    repeat_dict = {}
    for number in numbers:
        if number in repeat_dict.keys():
            repeat_dict[number] += 1
        else:
            repeat_dict[number] = 1
    return repeat_dict


def main():
    numbers = [1, 2, 3, 4, 5, 6, 5, 3, 4, 3, 3, 1]
    result = calc_repetition(numbers)
    print(result)


if __name__ == '__main__':
    main()
