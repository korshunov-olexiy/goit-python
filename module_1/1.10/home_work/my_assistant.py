from collections import UserDict
from inspect import getcallargs
from typing import List, Optional


def check_if_present_phone_number(func):
    '''Decorator for checking if the phone number is present'''
    def inner(*args, **kwargs):
        # getting default named attribute 'idx'
        kwargs['idx'] = getcallargs(func, *args, *kwargs)['idx']
        for i,phone in enumerate(args[0].phone):
            if phone.value == args[1]:
                kwargs['idx'] = i
                break
        return func(*args, **kwargs)
    return inner


class Field:
    '''Field class is parent for all fields in Record class'''
    def __init__(self, value: str):
        self.value = value.capitalize()


class Name(Field):
    '''Name class for storage name's field'''


class Phone(Field):
    '''Phone class for storage phone's field'''

    def __str__(self):
        return f"Phone: {self.value}"


class Record:
    """Record class responsible for the logic of adding/removing/editing fields
    Only one name but many phone numbers"""

    def __init__(self, name: str, phone: List[str] = None) -> None:
        if phone is None:
            self.phone = []
        else:
            self.phone = [Phone(one_phone) for one_phone in phone]
        self.name = Name(name)

    @check_if_present_phone_number
    def add_phone(self, phone_number: str, idx=-1) -> None:
        if idx == -1:
            self.phone.append(Phone(phone_number))

    @check_if_present_phone_number
    def delete_phone(self, phone: str, idx=-1) -> None:
        if idx != -1:
            self.phone.pop(idx)

    @check_if_present_phone_number
    def edit_phone(self, old_phone: str, new_phone: str, idx=-1) -> None:
        if idx != -1:
            self.phone[idx] = Phone(new_phone)

    def __str__(self):
        return f"Record of {self.name.value}, phones {[p.value for p in self.phone]}"


class AddressBook(UserDict):
    '''Add new instance of Record class in AddressBook'''

    def add_record(self, name: str, phones: list) -> None:
        new_record = Record(name, phones)
        self.data[new_record.name.value] = new_record

    def find_record(self, value: str) -> Optional[Record]:
        return self.data.get(value.capitalize())

    def delete_record(self, value: str) -> None:
        value = value.capitalize()
        if self.data.get(value):
            self.data.pop(value)

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    # USAGE EXAMPLE:
    book = AddressBook()
    book.add_record('seMeN', ["063 666 99 66", "048 722 22 22"])
    book.add_record("grySha", ["063 666 66 66", "048 222 22 22"])

    record = book.find_record("semen")
    print(111, record)
    book.delete_record("grYsha")

    print("#" * 10)
    print(book)
    print("#" * 10)
    record.delete_phone("048 222 22 22")
    record.add_phone('123-345-567')
    record.edit_phone("063 666 66 66", "067-666-66-66")
    print(record)
