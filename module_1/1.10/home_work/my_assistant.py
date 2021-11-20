from collections import UserDict
from typing import Optional, List


def capitalize_name(outer_method):
    '''Decorator for capitalize name attribute in method'''
    def inner_func(*args):
        if isinstance(args[1], list):
            return outer_method(args[0], [args[1][0].capitalize()] + args[1][1:])
        elif isinstance(args[1], str):
            return outer_method(args[0], args[1].capitalize())
        elif isinstance(args[0] == args[1]):
            self, other = args[0], args[1]
            self.value = self.value.capitalize()
            other.value = self.other.value.capitalize()
            return outer_method(self, other)
    return inner_func


def check_if_present_phone_number(func):
    '''Decorator for checking if the phone number is present'''
    def inner(*args, idx=-1):
        for i,p in enumerate(args[0].phone):
            if p.value == args[1]:
                return func(*args, idx=i)
        return func(*args, idx=idx)
    return inner

class Field:
    '''Field class is parent for all fields in Record class'''
    @capitalize_name
    def __init__(self, value: str):
        self.value = value


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
            self.phone = [Phone(p) for p in phone]
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

    @capitalize_name
    def add_record(self, record: list) -> None:
        new_record = Record(record[0], record[1:])
        self.data[new_record.name.value] = new_record

    @capitalize_name
    def find_record(self, value: str) -> Optional[Record]:
        return self.data.get(value)

    @capitalize_name
    def delete_record(self, value: str) -> None:
        if self.data.get(value):
            self.data.pop(value)

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    # USAGE EXAMPLE:
    book = AddressBook()
    book.add_record(["seMeN", "063 666 99 66", "048 722 22 22"])
    book.add_record(["grySha", "063 666 66 66", "048 222 22 22"])

    record = book.find_record("semen")
    book.delete_record("yehor")

    print("#" * 10)
    print(book)
    print("#" * 10)
    record.delete_phone("048 222 22 22")
    record.add_phone('123-345-567')
    record.edit_phone("063 666 66 66", "067-666-66-66")
    print(record)
