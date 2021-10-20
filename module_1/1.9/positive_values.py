'''
Создайте функцию positive_values и с помощью функции filter
отфильтруйте список payment по положительным значениям и верните его из функции.
'''
def positive_values(list_payment):
    return list(filter(lambda item: item > 0, list_payment))

# EXAMPLE:
print(positive_values([100, -3, 400, 35, -100]))
