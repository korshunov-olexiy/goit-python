'''
Разработайте две метода для сериализации и десериализации экземпляра класса Contacts,
с помощью пакета pickle и хранения полученных данных в бинарном файле.
Первый метод save_to_file сохраняет экземпляр класса Contacts в файл используя
метод dump пакета pickle. Имя файла хранится в атрибуте filename.
Второй метод read_from_file читает и возвращает экземпляр
класса Contacts (!!! т.е. self !!!)
из файла filename используя метод load пакета pickle.
'''

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.contacts = contacts
        self.filename = filename

    def save_to_file(self):
        with open(self.filename, 'wb') as fn:
            pickle.dump(self, fn)

    def read_from_file(self):
        with open(self.filename, 'rb') as fn:
            data = pickle.load(fn)
        return data


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(person_from_file)
