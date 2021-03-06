# -*- coding: utf-8 -*
# Дан список целых чисел. Отсортируйте его в порядке неубывания значений.
# Выведите полученный список на экран.
# Решите эту задачу при помощи алгоритма сортировки вставкой.
# Решение оформите в виде функции InsertionSort(A).
# В этой задаче нельзя пользоваться дополнительным списком операциями
# удаления и вставки элементов.

# Формат ввода
# Данные вводятся с клавиатуры или из файла input.txt.

# Формат вывода
# Данные выводятся на экран или в файл output.txt.

def InsertionSort(A):
    for i in range(1, len(A)):
        tmp = int(A[i])
        k = i
        while k > 0 and tmp < int(A[k - 1]):
            A[k] = A[k - 1]
            k -= 1
        A[k] = tmp
    return A

input_numbers = input().split()
for item in InsertionSort(input_numbers):
    print(item)