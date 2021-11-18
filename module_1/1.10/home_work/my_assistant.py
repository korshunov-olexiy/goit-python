from collections import UserDict


def check_if_present_phone(func):
    '''Decorator for checking if the phone number is present'''
    def inner(*args):
        phone_present = args[1] in args[0].phones.phones
        if func.__name__ == 'add_phone':
            if not phone_present:
                return func(*args)
        elif phone_present:
            return func(*args)
    return inner


class Record:
    """Record class responsible for the logic of adding/removing/editing fields
    Only one name but many phone numbers"""

    def __init__(self, name:str, phones=['']):
        self.name = Name(name)
        self.phones = Phone(name, phones)

    @check_if_present_phone
    def add_phone(self, phone):
        self.phones.phones.append(phone)

    @check_if_present_phone
    def del_phone(self, phone):
        self.phones.phones.remove(phone)

    @check_if_present_phone
    def change_phone(self, old_phone, new_phone):
        self.del_phone(old_phone)
        self.phones.phones.append(new_phone)



class Field:
    '''Field class is parent for all fields in Record class'''
    def __init__(self, name:str, phones=['']):
        self.value = name.capitalize()
        self.phones = phones


class Name(Field):
    '''Name class for storage name's field'''


class Phone(Field):
    '''Phone class for storage phone's field'''


class AddressBook(UserDict):
    '''Add new instance of Record class in AddressBook'''
    def add_record(self, record:Record):
        self.data[record.name.value] = record

    '''Change record name & attribute name in Name class'''
    def change_record_name(self, record_name:str, new_name:str):
        record_name = record_name.capitalize()
        new_name = new_name.capitalize()
        if self.data.get(record_name):
            # change name of record
            self.data[new_name] = self.data.pop(record_name)
            # change name in Name class
            self.data[new_name].name.value = new_name
            return True
        return False

    '''Find record by name'''
    def find_record(self, name):
        return self.data.get(name.capitalize(), None)



if __name__ == "__main__":
    # -=- Usage example -=-
    ab = AddressBook()
    john = Record('john', ['144-255', '202-324'])
    ab.add_record(john)
    bob = Record('bob', ['325-146'])
    bob.add_phone('55555')
    bob.add_phone('55555')
    bob.add_phone('55555')
    bob.change_phone('55555', '55555-5555555')
    bob.del_phone('55555-5555555')
    ab.add_record(bob)
    ab.change_record_name('bob', 'smith')
