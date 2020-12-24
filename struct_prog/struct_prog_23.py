# В заданной строке расположить в обратном порядке
# все слова. Разделителями слов считаются пробелы.
# [02-7.2-HL08]

string = 'My string is an example string'
string_split = string.split()
string_split = string_split[::-1]
string = ' '.join(string_split)
print(string)
