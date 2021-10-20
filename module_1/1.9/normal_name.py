'''
Разработайте функцию normal_name,
которая принимает список имен
и возвращает тоже список имен,
но уже с правильными именами с заглавной буквы.
'''
def normal_name(list_name):
    return list(map(lambda item: item.capitalize(), list_name))

# EXAMPLE:
print(normal_name(['kalina', 'malina', 'ochered']))
