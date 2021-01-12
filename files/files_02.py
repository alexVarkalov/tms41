# Создать текстовый файл и записать
# в него 6 строк. Записываемые строки
# вводятся с клавиатуры.


def main():
    with open('files_02.txt', 'w') as my_file:
        for _ in range(6):
            string = input('Enter your string: ')
            my_file.write(f'{string}\n')


if __name__ == '__main__':
    main()
