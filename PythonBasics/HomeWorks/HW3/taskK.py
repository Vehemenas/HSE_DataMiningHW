# -*- coding: utf-8 -*
# По данному натуральному n≤9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

# Входные данные
# Вводится натуральное число.

# Выходные данные
# Выведите ответ на задачу.

number = int(input())
s = ""
for i in range(1, number + 1):
    s = s + str(i)
    print(s)