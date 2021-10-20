'''
получить список из quantity случайных чисел без повторов
'''
from random import randrange, sample


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or max < 1 or min >= max or (quantity not in [5, 6]):
        return []
    digits = sorted(set([randrange(min, max)
                    for _ in range(quantity+10)]))[:quantity]
    return digits


print(get_numbers_ticket(1, -49, 5))


# [1, 3, 5, 7, 8, 9, 16, 17, 22, 22, 24, 29, 29, 36, 46]
# [3, 5, 29, 29, 36]
