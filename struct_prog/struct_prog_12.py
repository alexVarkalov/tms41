# Дан список целых чисел. Подсчитать
# сколько четных чисел в списке

my_list = [8, -7, -6, 7, 0, 7, -2, 6, 4, -6]
even_counter = 0
i = 0
while i != len(my_list):
    if my_list[i] % 2 == 0:  # if not my_list[i] % 2
        even_counter += 1
    i += 1
print(even_counter)
