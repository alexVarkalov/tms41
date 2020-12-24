# Получить на ввод количество рублей и копеек
# и вывести в правильной форме, например:
# 3 рубля, 1 рубль 25 копеек, 3 копейки

rubles = int(input("Enter rubles: "))
cents = int(input("Enter cents: "))
if cents >= 100:
    rubles += cents // 100
    cents %= 100

if rubles % 10 == 1 and rubles % 100 != 11:
    word_rubles = "Рубль"
elif 2 <= rubles % 10 <= 4 and (rubles % 100 <= 4 or rubles % 100 >= 22):
    word_rubles = "Рубля"
else:
    word_rubles = "Рублей"

if cents % 10 == 1 and cents % 100 != 11:
    word_cents = "Копейка"
elif 2 <= cents % 10 <= 4 and (cents <= 4 or cents >= 22):
    word_cents = "Копейки"
else:
    word_cents = "Копеек"

print(f'{rubles} {word_rubles}, {cents} {word_cents}')
