from collections import UserDict
from typing import List, Optional


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

    def get_phone_index(self, check_number: str) -> Optional[int]:
        """The function checks the user's phone number. 
        If the number is found, it returns its index; otherwise, None is."""
        try:
            return [one_phone.value for one_phone in self.phone].index(check_number)
        except ValueError:
            return None


    def add_phone(self, phone_number: str) -> None:
        index = self.get_phone_index(phone_number)
        if not index:
            self.phone.append(Phone(phone_number))

    def delete_phone(self, phone: str) -> None:
        index = self.get_phone_index(phone)
        if index:
            self.phone.pop(index)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        index = self.get_phone_index(old_phone)
        if  index and not self.get_phone_index(new_phone):
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
    record.add_phone('123-345-567-134-12')
    record.edit_phone("063 666 99 66", "067-666-66-66")
    print(record)
