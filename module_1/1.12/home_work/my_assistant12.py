from collections import UserDict
from datetime import datetime
from inspect import getcallargs
from typing import List, Optional
import pickle, pathlib


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
    def __init__(self, value):
        self.value = value
    
    @property
    def value(self):
        #if hasattr(self, '_value'):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(self, Phone):
            self._value = value if len(value) == 13 else ''
        elif isinstance(self, Birthday):
            try:
                dt = value.split('.')
                value = f"{int(dt[0]):02d}.{int(dt[1]):02d}.{int(dt[2])}"
                datetime.strptime(value, '%d.%m.%Y')
                self._value = value
            except:
                self._value = None
        else:
            self._value = value.capitalize()


class Name(Field):
    '''Name class for storage name's field'''


class Phone(Field):
    '''Phone class for storage phone's field'''

    def __str__(self):
        return f"Phone: {self.value}"


class Birthday(Field):
    '''Birthday class for storage birthday's field'''


class Record:
    """Record class responsible for the logic of adding/removing/editing fields
    Only one name but many phone numbers"""

    def __init__(self, name: str, phone: List[str] = None, birthday: str = None) -> None:
        if phone is None:
            self.phone = []
        else:
            self.phone = [Phone(p) for p in phone]
        self.name = Name(name)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self) -> Optional[str]:
        '''return number of days until the next birthday'''
        
        if not isinstance(self.birthday.value, type(None)):
            current_date = datetime.today()
            current_year = current_date.year
            birthday = datetime.strptime(f"{self.birthday.value[:6]}{current_year}", '%d.%m.%Y')
            if  birthday < current_date:
                birthday = birthday.replace(year=current_year+1)
            days = (birthday - current_date).days
            return f"{days} day(s)"
        return ''

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
        result = f"Record of {self.name.value}, "
        result += f"phones: {[p.value for p in self.phone]}"
        if not isinstance(self.birthday.value, type(None)):
            result += f", birthday: {self.birthday.value}"
            result += f", to birthday: {self.days_to_birthday()}"
        return result

class AddressBook(UserDict):
    '''Add new instance of Record class in AddressBook'''

    def __init(self):
        self.is_unpacking = False

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
        page = []
        for name, rec in self.items():
            page.append(f"{name}: {rec}")
            if len(page) == n:
                yield page 
                page = []
        if page:
            yield page

    def save_data(self, filename):
        with open(filename, 'wb') as fn:
            data = self.data.copy
            pickle.dump(data, fn)

    def load_data(self, filename):
        with open(filename, 'rb') as fn:
            self.data = pickle.load(fn)
        return self.data

    def __getstate__(self):
        attributes = self.data.copy()
        return attributes

    def __setstate__(self, value):
        self.data = value
        self.is_unpacking = True

    def __str__(self):
        return str([name.value for name, rec in self.data.items()])


if __name__ == '__main__':
    # USAGE EXAMPLE:
    cur_dir = pathlib.Path().cwd()
    data_file = cur_dir.joinpath("data.bin")
    book = AddressBook()
    if data_file.exists():
        book.load_data(data_file)
    print(book)
    book.add_record("seMeN", ["063 666 99 66", "048 722 22 22"], '1.12.2021')
    book.add_record("grySha", ["063 666 66 66", "048 222 22 22"], '01.01.1996')
    book.add_record("vasya", ["777 666 55545", "999 111 33323"], '23.04.1976')
    # print(book.data['Semen'])
    # print(book.data['Grysha'])
    # print(book.data['Vasya'])

    for rec in book.iterator(2):
        print(rec)

    record = book.find_record("semen")
    record.add_phone('344-55-678')
    #print(record)
    book.delete_record("seMEN")
    record.delete_phone("048 722 22 22")
    record.add_phone('123-345-567')
    record.edit_phone("063 666 66 66", "067-666-66-66")
    book.save_data(data_file)