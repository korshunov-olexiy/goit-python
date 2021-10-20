'''
Реализуйте вспомогательную функцию, которая будет формировать запрос на сервер в виде словаря.
Данная функцию make_request(keys, values), принимает два параметра в виде списков.
Функция должна создать словарь с ключами из списка keys и значениями из списка values.
    Порядок соответствия совпадает с индексами списков keys и data.
    Если длина keys и values не совпадают, верните пустой словарь.
'''


def make_request(keys, values):
    dict = {}
    if len(keys) != len(values):
        return dict
    for idx, key in enumerate(keys):
        dict[key] = values[idx]
    return dict


print(make_request(['ke1', 'key2', 'key3'], ['val1', 'val2', 'val3']))
