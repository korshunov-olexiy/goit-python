from collections import UserDict, UserList

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
class Phones(UserList):
    def add(self, value):
        self.data.append(value)

'''
добавление, удаление, редактирование
необязательных полей
и хранение обязательного поля name
'''
class Record:
    def __init__(self, name, phone = []):
        self.name = name
        phones = self.data.get('phones', Phones())
        phones.add(phone)
        #self.phones.append(Phones.add(phone))


class AddressBook(UserDict):
    # добавляет объект Record в self.data
    def add_record(self, record=Record):
        phones = self.data.get([record.phones], [])
        phones.append(record)
        self.data[record.phones] = phones
    
    def find_record(self, value):
        keys = []

