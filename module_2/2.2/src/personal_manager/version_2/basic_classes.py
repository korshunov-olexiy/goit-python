from abc import ABC, abstractmethod
from collections import UserDict
from typing import Union, List
from enum import Enum

from primitives_classes import *


class SpecifyAttrError(Exception):
    """"""


class RecordAttrs(Enum):
    """List of attributes for the Record class."""

    name = Name, str
    birthday = Birthday, str
    phone = Phone, list
    address = Address, list
    email = Email, list
    note = Note, list


class GetValues:
    """Input record datas from console"""

    def __init__(self, interface: object) -> None:
        self.interface = interface()

    def get_values(self):
        for attr in RecordAttrs:
            if attr.value[1] == str:
                while not hasattr(self, attr.name):
                    input_msg = self.interface.get_msg("Enter values ​​for the ", attr.name, attr.value[1])
                    try:
                        setattr(self, attr.name, attr.value[0](input_msg))
                    except (InvalidBirthdayValue) as err_msg:
                        print(err_msg)
            elif attr.value[1] == list:
                attr_values = []
                input_msg = self.interface.get_msg("Enter values ​​for the ", attr.name, attr.value[1])
                len_input_msg = len(input_msg)
                for item_attr in input_msg:
                    while not hasattr(self, attr.name) or len(self.name) != len_input_msg:
                        try:
                            attr_values.append(attr.value[0](item_attr.strip()))
                            break
                        except (InvalidPhoneNumber, InvalidEmailAddress, InvalidNoteValue) as err_msg:
                            print(err_msg)
                            item_attr = self.interface.get_msg("Enter values ​​for the ", attr.name, str)
                setattr(self, attr.name, attr_values)

    def __str__(self):
        result = []
        attrs_dict = {name: val for name, val in self.__dict__.items() if name != "interface"}
        max_attr_len = len(max(attrs_dict, key=len))+1
        for attr_name, attr_value in attrs_dict.items():
            if isinstance(attr_value, list):
                values = ', '.join([attr.value for attr in attr_value])
            elif hasattr(attr_value, "value"):
                values = attr_value.value
            result.append(f"{attr_name:<{max_attr_len}}: {values}")
        return "\n".join(result)


class Interface:
    @abstractmethod
    def get_msg(self, console_text: str, attr_name: str, type_return: Union[str, List[str]]) -> Union[str, List[str]]:
        """"""


class InterfaceCMD(Interface):
    """Console interface for getting values ​​from the user."""

    def get_msg(self, console_text: str, attr_name: str, type_return: Union[str, List[str]]) -> Union[str, List[str]]:
        """"""
        input_msg = input(f"{console_text}\"{attr_name}\":\n").strip()
        if type_return == list:
            input_msg = input_msg.split(";")
        return input_msg

# class Record:
#     """Record class for storing a record of the user."""

#     def __init__(self, values_attrs: object):
#         # if not values_attrs.__dict__.get("name"):
#         #     raise SpecifyAttrError("To create a contact, you must specify attribute \"name\".")
#         enum_attrs = RecordAttrs
#         for arg_name, arg_value in values_attrs.__dict__.items():
#             # if not self.validate_type(enum_attrs[arg_name].value[1], type(arg_value)):
#             #     raise SpecifyAttrError(f"The type of the attribute \"{arg_name}\" is not correct.")
#             if enum_attrs[arg_name].value[1] ==  list:
#                 items = []
#                 for val in arg_value:
#                     try:
#                         items.append(enum_attrs[arg_name].value[0](val))
#                     except (InvalidPhoneNumber, InvalidEmailAddress, InvalidNoteValue) as err_attr:
#                         print(f"{err_attr}")
#             elif enum_attrs[arg_name].value[1] ==  str:
#                 items = ""
#                 try:
#                     items = enum_attrs[arg_name].value[0](arg_value)
#                 except (InvalidBirthdayValue) as err_attr:
#                     print(f"{err_attr}")
#             if items:
#                 setattr(self, arg_name, items)

#     def validate_type(self, enum_type: Type[Any], attr_type: Type[Any]) -> bool:
#         return enum_type == attr_type

#     def __str__(self):
#         result = []
#         attrs_dict = self.__dict__
#         max_attr_len = len(max(attrs_dict, key=len))+1
#         for attr_name, attr_value in attrs_dict.items():
#             if isinstance(attr_value, list):
#                 values = ', '.join([attr.value for attr in attr_value])
#             elif hasattr(attr_value, "value"):
#                 values = attr_value.value
#             result.append(f"{attr_name:<{max_attr_len}}: {values}")
#         return "\n".join(result)


# class AddressBook(UserDict):
#     """Add new instance of Record class in AddressBook"""

#     def iterator(self, n: str = 1) -> List[str]:
#         separator, enter = "="*60, "\n"
#         yield from ([f"{separator}: {enter}{rec}" for name, \
#             rec in list(self.items())[i: i + n]] for i in range(0, len(self), n))

#     def add_record(self) -> None:
#         new_record = Record(*self.__get_params({"name": "", "phones": "", "birthday": "", "addresses": "", "emails": "", "notes": ""}))
#         while not new_record.name.value:
#             name_value = ''.join(self.__get_params({"name": ""}, "Username not recorded. Please, enter the ")).strip()
#             if name_value:
#                 new_record.name.value = name_value
#         while not hasattr(new_record, "birthday") or not new_record.birthday.value:
#             birthday_value = ''.join(self.__get_params({"date of birth": ""}, \
#                 "Date of birth not recorded. Please enter the correct ")).strip()
#             if birthday_value:
#                 new_record.birthday = Birthday(birthday_value)
#         self.data[new_record.name.value] = new_record


def standard_input():
    yield "Vasya"
    yield "22.02.995"
    yield "22.02.1995"
    yield "222-222-22-2;333-222-11-00"
    yield "222-222-22-22"
    yield "address #1"
    yield "em1@gmail.com"
    yield "note #1"


rec = GetValues(InterfaceCMD)
rec.get_values()
print("================================")
print(rec)
