from collections import UserDict
from typing import List, Optional


def get_phone_index(phone_obj: object, check_number: str) -> Optional[int]:
    """The function checks the user's phone number. 
    If the number is found, it returns its index; otherwise, None is."""
    for i,phone in enumerate(phone_obj.phone):
        if phone.value == check_number:
            return i
    return None


class Field:
    """Field class is parent for all fields in Record class"""
    def __init__(self, value: str):
        self.value = value.capitalize()


class Name(Field):
    """Name class for storage name's field"""


class Phone(Field):
    """Phone class for storage phone's field"""

    def __str__(self):
        return f"Phone: {self.value}"


class Record:
    """Record class responsible for the logic of adding/removing/editing fields
    Only one name but many phone numbers"""

    def __init__(self, name: str, phone: List[str] = None):
        if phone is None:
            self.phone = []
        else:
            self.phone = [Phone(one_phone) for one_phone in phone]
        self.name = Name(name)

    def add_phone(self, phone_number: str) -> None:
        index = get_phone_index(self, phone_number)
        if index == None:
            self.phone.append(Phone(phone_number))

    def delete_phone(self, phone: str) -> None:
        index = get_phone_index(self, phone)
        if index != None:
            self.phone.pop(index)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        index = get_phone_index(self, old_phone)
        if  index != None and get_phone_index(self, new_phone) == None:
            self.phone[index] = Phone(new_phone)

    def __str__(self):
        return f"Record of {self.name.value}, phones {[p.value for p in self.phone]}"


class AddressBook(UserDict):
    """Add new instance of Record class in AddressBook"""

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
    #book.delete_record("grYsha")

    record.delete_phone("048 722 22 22")
    record.add_phone('123-345-567')
    record.edit_phone("063 666 99 66", "067-666-66-66")
    print(record)
