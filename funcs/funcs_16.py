# Даны три слова. Выяснить, является ли хоть одно
# из них палиндромом ("перевертышем"), т. е. таким,
# которое читается одинаково слева направо и справа
# налево. (Определить функцию, позволяющую распознавать
# слова палиндромы.)[03-10.32]


def is_polindrom(word):
    word = word.lower()
    return word == word[::-1]


def is_polindrom_in_list(words):
    for word in words:
        if is_polindrom(word):
            return True
    return False


def main():
    print(is_polindrom_in_list(['aba', 'asdf', 'bbbccc']))
    print(is_polindrom_in_list(['abaa', 'asdf', 'bbbccc']))


if __name__ == '__main__':
    main()
