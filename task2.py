# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random as rn

numbers = list()

len_nums = int(input('Введите желаемую длину массива: '))

for i in range(0, len_nums+1):
    numbers.append(rn.randint(0, 9))

print(numbers)

seeking_num = int(input('Введите число, количество для которого необходимо найти ближайшее по значению число в списке: '))

if seeking_num in numbers:
    print(f'Искомое число {seeking_num} встречается в списке {numbers}')
else:
    diff = 10
    res_num = 10
    for i in numbers:
        if abs(seeking_num - i) < diff:
            diff = abs(seeking_num - i)
            res_num = i

    print(f'Число {res_num} наиболее близко к числу {seeking_num} из всего списка {numbers}')