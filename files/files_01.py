# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.

TEST_TASK = 4


def print_first_line(file_name):
    my_file = open(file_name)
    line = my_file.readline()
    if line:
        print(line)
    else:
        print('File is empty')
    my_file.close()


def print_fifth_line(file_name):
    my_file = open(file_name)
    i = 0
    while True:
        line = my_file.readline()
        if not line:
            print('File size is less than 5')
            break
        if i + 1 == 5:
            print(f'The 5th line: {line}')
            break
        i += 1
    my_file.close()


def print_first_five_lines(file_name):
    my_file = open(file_name)
    i = 0
    while True:
        line = my_file.readline()
        if not line:
            print('File size is less than 5')
            break
        if i >= 5:
            break
        i += 1
        print(f'Line #{i:02}: {line}')
    my_file.close()


def print_lines_from_s1_to_s2(file_name, s1, s2):
    my_file = open(file_name)
    i = 0
    if s1 > s2:
        print('Bad input')
        return
    while True:
        line = my_file.readline()
        if not line:
            break
        if s1 <= i + 1 <= s2:
            print(f'Line #{i+1:02}: {line}')
        i += 1
    my_file.close()


def print_entire_file(file_name):
    my_file = open(file_name)
    i = 0
    while True:
        line = my_file.readline()
        if not line:
            break
        i += 1
        print(f'Line #{i:02}: {line}')
    my_file.close()


def main():
    if not TEST_TASK or TEST_TASK == 1:
        print_first_line('files_01.txt')
    if not TEST_TASK or TEST_TASK == 2:
        print_fifth_line('files_01.txt')
    if not TEST_TASK or TEST_TASK == 3:
        print_first_five_lines('files_01.txt')
    if not TEST_TASK or TEST_TASK == 4:
        print_lines_from_s1_to_s2('files_01.txt', 1, 5)
    if not TEST_TASK or TEST_TASK == 5:
        print_entire_file('task_10_01.txt')


if __name__ == '__main__':
    main()
