# -*- coding: utf-8 -*
# Даны три натуральных числа a, b, c.
# Определите, существует ли треугольник с такими сторонами.
# Если треугольник существует, выведите строку YES, иначе выведите строку NO.
# Треугольник — это три точки, не лежащие на одной прямой.

# Входные данные
# Вводятся три натуральных числа.

# Выходные данные
# Выведите ответ на задачу.

a = int(input())
b = int(input())
c = int(input())

if a < b + c and  b < a + c and c < a + b:
    print("YES")
else:
    print("NO")