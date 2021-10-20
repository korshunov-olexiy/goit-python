'''
Необходимо реализовать функцию generator_numbers, которая будет парсить строку
и находить все целые числа в ней, и работая как генератор отдавать указанные числа
при обращении к ней в цикле.

Функция generator_numbers(string="") непосредственно распарсивает строку
и при помощи yield возвращает текущее число.
Функция sum_profit(string) суммирует числа, полученные от generator_numbers
и возвращает общую сумму прибыли из строки.
'''
import re

def generator_numbers(string=""):
    # для чисел float шаблон будет такой:
    # r'\d{1,}[.,]\d{1,}'
    for digit in re.findall(r'\d{1,}', string):
        yield digit

def sum_profit(string):
    return sum(map(int, generator_numbers(string)))

# EXAMPLE:
input_str = "The resulting profit was: from the southern possessions $ 100.0, from the northern colonies $500.20, and the king gave $1000.1."
print(sum_profit(input_str))
