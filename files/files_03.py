# В конец существующего текстового файла
# записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.


def main():
    with open('files_03.txt', 'a') as my_file:
        for _ in range(3):
            string = input('Enter your string: ')
            my_file.write(f'{string}\n')


if __name__ == '__main__':
    main()
