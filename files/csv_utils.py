# Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
# Удаление записи(по позиции, по-умолчанию последнюю).

import csv


def read_csv(filename):
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
        fields = rows[0]
        data = rows[1:]
    return fields, data


def prepare_csv_data(fileds, rows):
    list_fields = fileds.split(',')
    list_rows = []
    for row in rows:
        list_rows.append(row.split(','))
    return list_fields, list_rows


def print_csv(filename):
    fields, rows = read_csv(filename)
    for col in fields:
        print(col.ljust(30, " "), end='')
    print()
    for row in rows:
        for col in row:
            print(col.ljust(30, " "), end='')
        print()


def write_csv(filename, fields, rows):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def add_row_to_csv(filename, row, position=None):
    fields, rows = read_csv(filename)

    if position is None:
        rows.append(row.split(','))
    else:
        rows.insert(position - 1, row.split(','))

    write_csv(filename, fields, rows)


def del_row_from_csv(filename, position=None):
    fields, rows = read_csv(filename)

    if position is None:
        rows.pop()
    else:
        rows.pop(position - 1)

    write_csv(filename, fields, rows)
