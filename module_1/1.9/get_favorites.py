'''
Создайте функцию get_favorites(contacts), которая будет возвращать список
содержащий только избранные контакты. Используйте при этом функцию filter,
чтобы отфильтровать по полю favorite только избранные контакты
'''
def get_favorites(contacts):
    return list(filter(lambda item: item['favorite'] == True, contacts))


# EXAMPE:

contacts = [{
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": True,
    },
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }]

print( get_favorites(contacts) )