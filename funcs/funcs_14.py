# Написать 12 функций по переводу:
# Дюймы в сантиметры, Сантиметры в дюймы, Мили в километры,
# Километры в мили, Фунты в килограммы, Килограммы в фунты,
# Унции в граммы, Граммы в унции, Галлон в литры, Литры в галлоны,
# Пинты в литры, Литры в пинты
# Примечание: функция принимает на вход число и возвращает
# конвертированное число

# Написать программу, со следующим интерфейсом: пользователю
# предоставляется на выбор 12 вариантов перевода(описанных в первой
# задаче). Пользователь вводит цифру от одного до двенадцати. После
# программа запрашивает ввести численное значение. Затем программа
# выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из
# программы - “0”.

def inchs_to_centimeters(n):
    """Return argument n as a representation in centimeters"""
    return round(n * 2.54, 2)


def centimeters_to_inchs(n):
    """Returns argument n as a representation in Imperial inchs"""
    return round(n / 2.54, 2)


def miles_to_km(n):
    """Returns argument n as a representation in kilometers"""
    return round(n * 1.609, 2)


def km_to_miles(n):
    """Returns argument n as a representation in standard land miles"""
    return round(n / 1.609, 2)


def pounds_to_kilos(n):
    """Returns argument n as a representation in kilograms"""
    return round(n * 0.453592, 2)


def kilos_to_pounds(n):
    """Returns argument n as a representation in English pounds"""
    return round(n / 0.453592, 2)


def ounces_to_grams(n):
    """Returns argument n as a representation in grams"""
    return round(n * 28.3495, 3)


def grams_to_ounces(n):
    """Returns argument n as a representation in troy ounces"""
    return n / 28.3495


def gallons_to_liters(n):
    """Returns argument n as a representation in liters"""
    return round(n * 3.78541, 2)


def liters_to_gallons(n):
    """Returns argument n as a representation in American gallons"""
    return round(n / 3.8541, 2)


def pints_to_liters(n):
    """Returns argument n as a representation in liters"""
    return round(n * 0.658261, 2)


def liters_to_pints(n):
    """Returns argument n as a representation in English pints"""
    return round(n / 0.658261, 2)


while True:
    print(
        '''Функции конвертации:
      1)Дюймы в сантиметры
      2)Сантиметры в дюймы
      3)Мили в километры
      4)Километры в мили
      5)Фунты в килограммы
      6)Килограммы в фунты
      7)Унции в граммы
      8)Граммы в унции
      9)Галлоны в литрыt
      10)Литры в галлоны
      11)Пинты в литры
      12)Литры в пинты'''
    )
    case = int(input("Введите код функции, 0 для выхода: "))
    if case == 0:
        break
    elif case == 1:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {inchs_to_centimeters(i)}')
    elif case == 2:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {centimeters_to_inchs(i)}')
    elif case == 3:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {miles_to_km(i)}')
    elif case == 4:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {km_to_miles(i)}')
    elif case == 5:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {pounds_to_kilos(i)}')
    elif case == 6:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {kilos_to_pounds(i)}')
    elif case == 7:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {ounces_to_grams(i)}')
    elif case == 8:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {grams_to_ounces(i)}')
    elif case == 9:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {gallons_to_liters(i)}')
    elif case == 10:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {liters_to_gallons(i)}')
    elif case == 11:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {pints_to_liters(i)}')
    elif case == 12:
        i = float(input("Введите число для конвертации: "))
        print(F'Результат: {liters_to_pints(i)}')
    else:
        print('Невыерный код!')
