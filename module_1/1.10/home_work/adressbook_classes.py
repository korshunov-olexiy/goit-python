from collections import UserDict


class Record:
    """Record class responsible for the logic of adding/removing/editing fields
    Only one name but many phone numbers"""

    def __init__(self, name, phones=['']):
        self.name = Name(name)
        #self.phone = list(map(lambda p: Phone(name, p), phone))
        self.phones = Phone(name, phones)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def del_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, old_phone_index, new_phone):
        self.phones[old_phone_index] = Phone(new_phone)



class Field:
    '''Field class is parent for all fields in Record class'''
    def __init__(self, name, phones=['']):
        self.value = name.capitalize()
        self.phones = phones


class Name(Field):
    '''Name class for storage name's field'''
    def __init__(self, name):
        # reload parent dunder method __init__
        super().__init__(name)


class Phone(Field):
    '''Phone class for storage phone's field'''
    def __init__(self, name, phone):
        super().__init__(name, phone)


class AddressBook(UserDict):
    """All contacts data"""
    # передаем в add_record !!объект Record
    def add_record(self, record:Record):
        self.data[record.name.value] = record

    def change_record(self, record):
        for this_name, this_record in self.data.items():
            if this_name == record[0]:
                contact_phones = list(map(lambda phone_number: phone_number.phone, this_record.phone))
                if record[1] not in contact_phones:
                    ''''''
                    #raise UnknownPhoneError
                self.data[this_name].change_phone(contact_phones.index(record[1]), record[2])
                return self.data[this_name]
        # raise UnknownContactError

    def find_record(self, required_name):
        for this_name, this_record in self.data.items():
            if this_name == required_name:
                return this_record
        return None



if __name__ == "__main__":
    # -=- Usage example -=-
    ad = AddressBook()
    john = Record('john', ['144-255', '202-324'])
    #print('john:', john.phones.phones)
    ad.add_record(john)
    bob = Record('bob', ['325-146'])
    ad.add_record(bob)
    for name, rec in ad.data.items():
        print(name, rec.name.value, rec.phones.phones)
        #print(name, rec.name.value, ', '.join([r.value for r in rec.phone]))
    # add new field for user john in address book
    #john.add_field('address', 'Kurska, 56')
    # edit field for user john in address book
    #john.edit_field('address', 'Illinska, 156')
