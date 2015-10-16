# -*- coding: utf-8 -*
# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите an не используя циклы и стандартную функцию pow, а используя рекуррентное соотношение a^n=a*a^(n−1).
# Решение оформите в виде функции power(a, n).

# Входные данные
# Вводятся действительное положительное число a и целое неотрицательное число n.

# Выходные данные
# Выведите ответ на задачу.

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

a = float(input())
n = int(input())

print(power(a, n))