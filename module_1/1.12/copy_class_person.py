'''
Для копирования экземпляра класса Person,
реализуйте функцию copy_class_person.
В качестве параметра она принимает экземпляр
класса person, и возвращает "поверхностную" копию
объекта с помощью функции copy из пакета copy.
'''

import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)

