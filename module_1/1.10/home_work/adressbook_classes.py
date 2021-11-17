from collections import UserDict


class Record:
    """Record class responsible for the logic of adding/removing/editing fields
    Only one name but many phone numbers"""

    def __init__(self, name:str, phones=['']):
        self.name = Name(name)
        self.phones = Phone(name, phones)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def del_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, old_phone_index, new_phone):
        self.phones[old_phone_index] = Phone(new_phone)



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
    def find_record(self, required_name:str):
        return self.data.get(required_name.capitalize(), None)



if __name__ == "__main__":
    # -=- Usage example -=-
    ab = AddressBook()
    john = Record('john', ['144-255', '202-324'])
    #print('john:', john.phones.phones)
    ab.add_record(john)
    bob = Record('bob', ['325-146'])
    ab.add_record(bob)
    for name, rec in ab.data.items():
        print(name, rec.name.value, rec.phones.phones)
    
    ab.change_record_name('bob', 'smith')
    print(ab.__dict__)
    print(ab.find_record('smith').name.value)
    # add new field for user john in address book
    #john.add_field('address', 'Kurska, 56')
    # edit field for user john in address book
    #john.edit_field('address', 'Illinska, 156')
