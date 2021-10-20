def get_grade(key):
    ects_value = {'F': 1, 'FX': 2, 'E': 3,
                  'D': 3, 'C': 4, 'B': 5, 'A': 5}
    return ects_value.get(key)


def get_description(key):
    ects_desc = {'F': 'неудовлетворительно', 'FX': 'неудовлетворительно', 'E': 'достаточно',
                 'D': 'удовлетворительно', 'C': 'хорошо', 'B': 'очень хорошо', 'A': 'отлично'}
    return ects_desc.get(key)


print(get_grade('B'))
