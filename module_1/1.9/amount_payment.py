'''
Просуммируйте положительные значения списка
и верните их сумму
'''
from functools import reduce


def amount_payment(payment):
    return reduce(lambda x, y: x + y if y >= 0 else x, payment, 0)


# EXAMPLE:
payment = [1, -3, 4, -5, 10]
print(amount_payment(payment))
