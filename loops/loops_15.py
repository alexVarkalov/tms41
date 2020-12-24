# Написать игру. Пользователь должен угадать число.
# Сперва вводиться диапазон угадывания. После колличество попыток.
# В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или меньше
# искомое число). Если за указанное количество попыток число не
# угадано - выводить: You are the loser и правильное число.

from random import randint

guess_from = int(input('guess from: '))
guess_to = int(input('guess to: '))
amount_of_try = int(input('amount of try: '))
rand_number = randint(guess_from, guess_to)

for i in range(amount_of_try):
    number = int(input('Guess the number: '))
    if number == rand_number:
        print('You are the winner')
        break
    elif number < rand_number:
        print('True number is bigger')
    else:
        print('True number is smaller')
else:
    print('You are the loser')
