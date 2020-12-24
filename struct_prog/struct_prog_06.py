# Ввести строку. Если длина строки больше 10 символов,
# то создать новую строку с 3 восклицательными знаками
# в конце  ('!!!') и вывести на экран.
# Если меньше 10, то вывести на экран второй символ строки

string = input('Enter your string: ')
string_len = len(string)
if string_len > 10:
    new_string = string + '!!!'
    print(new_string)
elif string_len < 10:
    print(string[1])
