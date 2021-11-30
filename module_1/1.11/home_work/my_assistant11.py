from collections import UserDict
from datetime import datetime
from typing import List, Optional


class InvalidPhoneNumber(Exception):
    """"""

class Field:
    """Field class is parent for all fields in Record class"""
    def __init__(self, value):
        self.value = value

class Name(Field):
    """Name class for storage name"s field"""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value.capitalize()


class Phone(Field):
    """Phone class for storage phone"s field"""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if len(value) == 13:
            self._value = value
        else:
            raise InvalidPhoneNumber

    def __str__(self):
        return f"Phone: {self.value}"


class Birthday(Field):
    """Birthday class for storage birthday"s field"""
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        try:
            dt = value.split(".")
            value = f"{int(dt[0]):02d}.{int(dt[1]):02d}.{int(dt[2])}"
            datetime.strptime(value, "%d.%m.%Y")
            self._value = value
        except:
            self._value = None


class Record:
    """Record class responsible for the logic of adding/removing/editing fields
    Only one name but many phone numbers"""

    def __init__(self, name: str, phone: List[str] = None, birthday: str = None) -> None:
        self.phone = []
        if phone is None:
            self.phone = []
        else:
            for one_phone in phone:
                try:
                    self.phone.append(Phone(one_phone))
                except InvalidPhoneNumber:
                    print(f"The phone number {one_phone} is invalid")
        self.name = Name(name)
        self.birthday = Birthday(birthday)

    def get_phone_index(self, check_number: str) -> Optional[int]:
        """The function checks the user"s phone number. 
        If the number is found, it returns its index; otherwise, None is."""
        try:
            return [one_phone.value for one_phone in self.phone].index(check_number)
        except ValueError:
            return None

    def days_to_birthday(self) -> str:
        """return number of days until the next birthday"""
        
        if not isinstance(self.birthday.value, type(None)):
            current_date = datetime.today()
            current_year = current_date.year
            birthday = datetime.strptime(f"{self.birthday.value[:6]}{current_year}", "%d.%m.%Y")
            if  birthday < current_date:
                birthday = birthday.replace(year=current_year+1)
            days = (birthday - current_date).days
            return f"{days} day(s)"
        return ""

    def add_phone(self, phone_number: str) -> None:
        index = self.get_phone_index(phone_number)
        if index == None:
            try:
                self.phone.append(Phone(phone_number))
            except InvalidPhoneNumber:
                print(f"The phone number {phone_number} is invalid")

    def delete_phone(self, phone: str) -> None:
        index = self.get_phone_index(phone)
        if index != None:
            self.phone.pop(index)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        index = self.get_phone_index(old_phone)
        if index == None:
            try:
                self.phone[index] = Phone(new_phone)
            except InvalidPhoneNumber:
                print(f"The phone number {new_phone} is invalid")

    def __str__(self):
        result = f"Record of {self.name.value}, "
        result += f"phones: {[one_phone.value for one_phone in self.phone]}"
        if not isinstance(self.birthday.value, type(None)):
            result += f", birthday: {self.birthday.value}"
            result += f", to birthday: {self.days_to_birthday()}"
        return result

class AddressBook(UserDict):
    """Add new instance of Record class in AddressBook"""

    def add_record(self, name: str, phones: List[str] = None, birthday: str = None) -> None:
        new_record = Record(name, phones, birthday)
        self.data[new_record.name.value] = new_record

    def find_record(self, value: str) -> Optional[Record]:
        return self.data.get(value.capitalize())

    def delete_record(self, value: str) -> None:
        value = value.capitalize()
        if self.data.get(value):
            self.data.pop(value)

    def iterator(self, n: str = 1) -> List[str]:
        for i in range(0, len(self), n):
            yield [f"{name}: {rec}" for name,rec in list(self.items())[i:i+n]]

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    # USAGE EXAMPLE:
    book = AddressBook()
    book.add_record("seMeN", ["063 666 99 66", "048 722 22", "123 456 789 1"], "01.12.2021")
    book.add_record("grySha", ["063 666 66 66", "048 222 22 22"], "01.01.1996")
    book.add_record("vasya", ["777 666 55545", "999 111 33323"], "23.04.1976")
    book.add_record("petya", ["111 222 333 444", "800 546 342"], "13.04.1996")

    record = book.find_record("semen")
    record.add_phone("344-55-678111")
    # #print(record)
    # book.delete_record("seMEN")
    #record.delete_phone("344-55-678111")
    # record.add_phone("123-345-567")
    record.edit_phone("344-55-678111", "067-666-66-6")

    for rec in book.iterator(2):
            print(rec)
