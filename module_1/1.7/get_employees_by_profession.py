'''
Выдать из файла path список имен через пробел
чья профессия = profession
'''


def standard_input():
    yield "get_employees.txt"


def get_employees_by_profession(path, profession):
    lst = []
    with open(path, 'r') as fr:
        content = ''.join(fr.readlines()).splitlines()
    for worker, prof in [card.split() for card in content]:
        if prof == profession:
            lst.append(worker)
    return ' '.join(lst)


print(get_employees_by_profession(input(), 'cook'))
