'''
С помощью коллекции deque реализуйте структуру данных FIFO.
Создайте переменную fifo содержащую коллекцию deque.
Ограничьте ее размер с помощью константы MAX_LEN.
Функция push добавляет значение element в конец списка fifo.
Функция pop достает и возвращает первое значение из списка fifo
'''
from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)


def pop():
    return fifo.popleft()
