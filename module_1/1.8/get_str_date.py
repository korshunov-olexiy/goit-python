'''
Разработайте функцию get_str_date(date),
которая будет преобразовывать дату из базы данных
в формате ISO "2021-05-27 17:08:34.149Z"
в строковое представление "Thursday 27 May 2021" —
день недели, число, месяц и год. Преобразованное значение
функция должна вернуть при вызове.
ДОКУМЕНТАЦИЯ:
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
'''
from datetime import datetime


def get_str_date(date):
    db_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%fZ")
    return db_date.strftime('%A %d %B %Y')


print(get_str_date("2021-05-27 17:08:34.149Z"))
