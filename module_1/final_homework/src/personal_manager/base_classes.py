import re
from datetime import datetime
from typing import List, Optional


class InvalidPhoneNumber(Exception):
    """Exception in case of incorrect phone number input"""


class InvalidEmailAddress(Exception):
    """Exception in case of incorrect E-mail input"""


class Field:
    """Field class is a parent for all fields in Record class"""
    def __init__(self, value):
        self.value = value


class Name(Field):
    """Name class for storage name's field"""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value.capitalize()


class Phone(Field):
    """Phone class for storage phone's field"""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if len(value) == 13:
            self._value = value
        else:
            raise InvalidPhoneNumber

    def __str__(self) -> str:
        return self.value


class Email(Field):
    """Email class for storage email's field"""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.__check_email(value):
            self._value = value
        else:
            raise InvalidEmailAddress

    def __check_email(self, email: str) -> bool:
        matched = re.match(r"[a-z][a-z|\d._]{1,}@[a-z]{1,}\.\w{2,}", email, re.IGNORECASE)
        return bool(matched)

    def __str__(self) -> str:
        return self.value


class Tag(Field):
    """Tag class for storage tag's field"""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Note(Field):
    """Note class for storage note's field"""
    def __init__(self, value, tags: Optional[List[str]] = None):
        self._created_at = datetime.today()
        self.tag = []
        if tags:
            for one_tag in tags:
                self.tag.append(Tag(one_tag))
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self) -> str:
        if self.tag:
            return ", ".join([f"created at {str(self._created_at)}:", \
                self.value, f"tags: {', '.join([tag.value for tag in self.tag])}"])
        else:
            return f"created at {str(self._created_at)}: {self.value}"


class Address(Field):
    """Address class for storage address's field"""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self) -> str:
        return self.value


class Birthday(Field):
    """Birthday class for storage birthday's field"""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            self._value = datetime.strptime(value, "%d.%m.%Y").strftime("%d.%m.%Y")
        except ValueError:
            print(f" \"{value}\" --> Incorrect input format. Record can’t be made.")
            self._value = ''

    def __str__(self) -> str:
        return self.value
