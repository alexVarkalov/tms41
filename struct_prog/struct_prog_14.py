# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1
#
# Примечание: Во всех задачах предоставить 2 решения.
# Одно с использованием цикла while,
# другое с использованием цикла for с параметром.
# Оба решения предоставить в одном файле.


my_list = [1, 'a', 3.5, 7, False, 'b', True, -10, -2]
my_list_len = len(my_list)

while_new_list = []
i = 0
while i < my_list_len:
    if i + 1 == my_list_len:
        while_new_list.append(my_list[0])
    else:
        while_new_list.append(my_list[i+1])
    i += 1
print(while_new_list)

for_new_list = []
for i in range(my_list_len):
    if i + 1 == my_list_len:
        for_new_list.append(my_list[0])
    else:
        for_new_list.append(my_list[i+1])
print(for_new_list)

easy_new_list = my_list[1:]
easy_new_list.append(my_list[0])
print(easy_new_list)
