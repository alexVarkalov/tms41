# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки. Если нет, то получить
# номер первой строки, в которой эти файлы отличаются друг
# от друга.[03-15.31]

with open('files_06_01.txt') as file1, open('files_06_02.txt') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()
for i in range(len(lines1)):
    if lines1[i] != lines2[i]:
        print(f'index is {i}')
        break
else:
    print('files are equal')
