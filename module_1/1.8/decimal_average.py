'''
Создайте функцию decimal_average(number_list, signs_count),
которая будет вычислять среднее арифметическое типа Decimal
с количеством значащих цифр signs_count.
'''
from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    number_list = list(map(Decimal, number_list))
    return sum(number_list)/len(number_list)


lst = [3, 5, 77, 23, 0.57]
print(decimal_average(lst, 6))
