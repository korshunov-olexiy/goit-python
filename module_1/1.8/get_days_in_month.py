'''Напишите функцию для определения количества дней в конкретном месяце.
Ваша функция должна принимать два параметра: номер месяца в виде целого
числа в диапазоне от 1 до 12 и год, состоящий из четырех цифр. Убедитесь,
что функция корректно обрабатывает февраль високосного года.'''

import calendar


def get_days_in_month(month, year):
    return calendar.monthrange(year, month)[1]


print(get_days_in_month(2, 2024))
