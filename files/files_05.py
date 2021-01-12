# Имеется текстовый файл. Все четные строки этого
# файла записать во второй файл, а нечетные —
# в третий файл. Порядок следования строк
# сохраняется.[03-15.29]

with open('files_05.txt') as input_file:
    with open('files_05_even.txt', 'w') as even_file:
        with open('files_05_odd.txt', 'w') as odd_file:
            lines = input_file.readlines()
            for i, line in enumerate(lines):
                if i % 2 == 1:
                    odd_file.write(line)
                else:
                    even_file.write(line)
            # odd_file.writelines(lines[1::2])
            # even_file.writelines(lines[::2])
