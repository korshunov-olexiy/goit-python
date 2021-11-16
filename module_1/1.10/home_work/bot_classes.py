from collections import UserDict


class Field:
    '''Field class is parent for all fields in Record class'''
    def __init__(self, value, phones=None):
        self.value = value
        self.phones = phones


class Name(Field):
    '''Name class for storage name's field'''
    def __init__(self, value):
        super().__init__(value, phones=None)


class Phone(Field):
    '''Phone class for storage phone's field'''
    def __init__(self, values):
        super().__init__(values, phones=values)


class Record:
    '''Record class responsible for the logic of adding/removing/editing fields'''
    def __init__(self, name, phones = []):
        self.name = Name(name)
        self.phones = []
        self.phones.append(Phone(phones))
        #self.data = {'name': name, 'phone': phones}
    
    def add_field(self, field_name, value):
        self.data.update({field_name: value})
    
    def del_field(self, field_name):
        self.data.pop(field_name)
    
    def edit_field(self, field_name, value):
        self.data[field_name] = value


class AddressBook(UserDict):
    def add_record(self, user_name, phones = []):
        record = Record(user_name, phones)
        self.data.update({user_name: record})
        return record



if __name__ == "__main__":
    # -=- Usage example -=-
    # create address book
    ad = AddressBook()
    # add user in address book
    john = ad.add_record('john')
    print(john.name.value)
    # add another user in address book
    bob = ad.add_record('bob')
    # add new field for user john in address book
    john.add_field('address', 'Kurska, 56')
    # edit field for user john in address book
    john.edit_field('address', 'Illinska, 156')
