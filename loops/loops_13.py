# Создать список с фамилиями.
# Вывести все фамилии, которые
# начинаются на П и заканчиваются на а

lastnames = ['Петрова', 'Сидорова']

for lastname in lastnames:
    if lastname[0] == 'П' and lastname[-1] == 'а':
        print(lastname)
