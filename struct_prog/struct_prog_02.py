# Ввести строку с клавиатуры. Вернуть результат
# логического выражения: длина строки не меньше 8
# или в строке есть “Alex”.

string = input('enter string: ')
print(len(string) >= 8 or 'ALex' in string)
