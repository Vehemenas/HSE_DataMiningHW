# -*- coding: utf-8 -*
# Даны два списка чисел, которые могут содержать до 100000 чисел каждый.
# Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

# Входные данные
# Вводятся два списка чисел. Все числа каждого списка находятся на отдельной строке.

# Выходные данные
# Выведите ответ на задачу.

first_set = set(map(int, input().split(" ")))
second_set = set(map(int, input().split(" ")))

print(len(first_set & second_set))