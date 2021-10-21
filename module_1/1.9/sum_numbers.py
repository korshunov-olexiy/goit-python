'''
Для списка numbers подсчитать сумму элементов с помощью функции reduce.
'''
from functools import reduce


def sum_numbers(numbers):
    return reduce(lambda x,y: x+y, numbers)


# EXAMPLE:
numbers = [3, 4, 6, 9, 34, 12]
print(sum_numbers(numbers))
