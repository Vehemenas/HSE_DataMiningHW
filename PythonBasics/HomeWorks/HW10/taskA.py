# -*- coding: utf-8 -*
# Напишите программу, которая определяет, сколько раз встречается заданное число x в данном массиве.

# Формат ввода
# В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.
# Во второй строке вводятся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
# В третьей строке содержится одно целое число x , не превосходящее по модулю 1000.

# Формат вывода
# Вывести одно число – сколько раз встречается x в данном массиве.


tmp = input().strip()
numbers = map(int, input().strip().split())
find_nub = int(input())
counter = 0
for i in numbers:
    if i == find_nub:
        counter += 1
print(counter)
