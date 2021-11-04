'''Разработайте две функции для сериализации и
десериализации списка контактов, с помощью
пакета json и хранения полученных данных
в бинарном файле.
Список контактов должен храниться по ключу
"contacts", а не просто сохранить его в файл.'''

import json


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as fn:
        json.dump({'contacts': contacts}, fn)


def read_contacts_from_file(filename):
    with open(filename, 'r') as fn:
        data = json.load(fn)
    return data['contacts']

contacts = {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }


write_contacts_to_file('contacts.json', contacts)

print(read_contacts_from_file('contacts.json'))
