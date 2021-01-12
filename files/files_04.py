# Имеется текстовый файл. Переписать
# в другой файл все его строки с
# заменой в них символа 0 на символ
# 1 и наоборот. [03-15.28]


def main():
    new_lines = []
    with open('files_04_in.txt') as input_file:
        old_lines = input_file.readlines()

    for old_line in old_lines:
        new_line = ''
        for char in old_line:
            # if char == '0':
            #     new_line += '1'
            # elif char == '1':
            #     new_line += '0'
            # else:
            #     new_line += char
            new_line += '0' if char == '1' else '1' if \
                char == '0' else char
        new_lines.append(new_line)

    with open('files_04_out.txt', 'w') as output_file:
        output_file.writelines(new_lines)


if __name__ == '__main__':
    main()
