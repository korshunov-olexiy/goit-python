'''
С помощью коллекции deque реализуйте структуру данных LIFO.
Создайте переменную lifo содержащую коллекцию deque.
Ограничьте ее размер с помощью константы MAX_LEN.
Функция push добавляет значение element в начало списка lifo.
Функция pop достает и возвращает первое значение из списка lifo
'''
from collections import deque

MAX_LEN = 5

lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)


def pop():
    return lifo.popleft()


d = lifo
push(12)
print(d)
