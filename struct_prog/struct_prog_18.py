# Два натуральных числа называют дружественными,
# если каждое из них равно сумме всех делителей
# другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне
# от 200 до 300. [02-3.2-HL02]

n = int(input('n = '))
m = int(input('m = '))
numbers_with_dividers = []
list_of_numbers = range(n, m + 1)
if 0 < n < m:
    for number in list_of_numbers:
        sum_of_dividers = 0
        for i in range(1, number // 2 + 1):
            if number % i == 0:
                sum_of_dividers += i
        if sum_of_dividers in list_of_numbers:
            numbers_with_dividers.append((number, sum_of_dividers))
result = []

for number, dividers in numbers_with_dividers:
    if (dividers, number) in numbers_with_dividers and \
            dividers not in result and dividers != number:
        result.append(dividers)
print(result)
