# Написать функции по работе с csv файлами в файле csv_utils.py.
# Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
# Удаление записи(по позиции, по-умолчанию последнюю).
# В файле files_08 импортировать функции. С помощью функций создать
# файл с информацией о товарах(Имя товара, цена, количество, комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.

from files.csv_utils import (
    write_csv,
    print_csv,
    prepare_csv_data,
    add_row_to_csv,
    del_row_from_csv,
)


def main():
    fields = 'Product Name,Price,Amount,Comment'
    rows = [
        'Apple,1.5,10,With worms (O_o)',
        'Lemon,2,15,Sour',
        'Tomato,1.75,20,Red',
        'Cucumber,0.75,25,Prickly',
    ]
    fields, rows = prepare_csv_data(fields, rows)
    write_csv('files_08.csv', fields, rows)

    print_csv('files_08.csv')

    new_product_info = 'Potato,0.5,100,Young potaty :3'
    add_row_to_csv('files_08.csv', new_product_info)
    print('-' * 10 + 'ADD' + '-' * 10)
    print_csv('files_08.csv')
    del_row_from_csv('files_08.csv', 3)
    print('-' * 10 + 'DEL' + '-' * 10)
    print_csv('files_08.csv')


if __name__ == '__main__':
    main()
