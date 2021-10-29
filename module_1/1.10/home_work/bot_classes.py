from collections import UserDict

'''
обязательное поле с именем
'''
class Name:
    pass

'''
родительский класс для всех полей
'''
class Field:
    pass


'''
Не обязательное поле с телефоном
и таких одна запись (Record) может содержать несколько полей
'''
class Phone:
    pass

'''
добавление, удаление, редактирование
необязательных полей
и хранение обязательного поля name
'''
class Record:
    def __init__(self, name, phone = Phone):
        self.name = name
        self.phones.append(phone)


class AddressBook(UserDict):
    # добавляет объект Record в self.data
    def add_record(self, record=Record):
        phones = self.data.get([record.phones], [])
        phones.append(record)
        self.data[record.phones] = phones
    
    def find_record(self, value):
        keys = []

