# -*- coding: utf-8 -*
# По данному натуральном n вычислите сумму 1!+2!+3!++n!. В решении этой задачи можно использовать только один цикл.

# Входные данные
# Вводится натуральное число n.

# Выходные данные
# Выведите ответ на задачу.

import math
num = int(input())
s = 0
for i in range(1, num+1):
    s = s + math.factorial(i)
print(s)