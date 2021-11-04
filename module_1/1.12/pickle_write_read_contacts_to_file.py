'''Разработайте две функции для сериализации и
десериализации списка контактов, с помощью
пакета pickle и хранения полученных данных
в бинарном файле.'''

import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as f_wb:
        pickle.dump(contacts, f_wb)


def read_contacts_from_file(filename):
    with open(filename, 'rb') as f_rb:
        data = pickle.load(f_rb)
    return data

contacts = {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }


write_contacts_to_file('contacts.bin', contacts)
print(read_contacts_from_file('contacts.bin'))
