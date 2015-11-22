# -*- coding: utf-8 -*
# Реализуйте структуру данных "очередь".
# Напишите программу, содержащую описание очереди и моделирующую работу очереди,
# реализовав все указанные здесь методы.
# Программа считывает последовательность команд и в зависимости от команды
# выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку.
# Возможные команды для программы:

# push n
# Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.
# pop
# Удалить из очереди первый элемент. Программа должна вывести его значение.
# front
# Программа должна вывести значение первого элемента, не удаляя его из очереди.
# size
# Программа должна вывести количество элементов в очереди.
# clear
# Программа должна очистить очередь и вывести ok.
# exit
# Программа должна вывести bye и завершить работу.

# Гарантируется, что набор входных команд удовлетворяет следующим требованиям:
# максимальное количество элементов в очереди в любой момент не превосходит 100,
# все команды pop и front корректны, то есть при их исполнении в очереди содержится хотя бы один элемент.

# Формат ввода
# Вводятся команды управления очередью, по одной на строке

# Формат вывода
# Требуется вывести протокол работы с очередью, по одному сообщению на строке


def push(queue, val):
    queue.append(val)
    print("ok")

def pop(queue):
    print(queue.pop(0))


def front(queue):
    print(queue[0])


def size(queue):
    print(len(queue))


def clear(queue):
    queue[:] = []
    print("ok")

queue = []

while (True):
    input_cmd = input().strip().split()
    function = input_cmd[0]
    if function == "exit":
        print("bye")
        break
    elif function == "push":
        push(queue, input_cmd[1])
    elif function == "pop":
        pop(queue)
    elif function == "front":
        front(queue)
    elif function == "size":
        size(queue)
    elif function == "clear":
        clear(queue)