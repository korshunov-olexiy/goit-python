from difflib import get_close_matches
from enum import Enum
from pathlib import Path
from collections import UserDict
import pickle
from pick import pick

from interface_cmd import *
from primitives_classes import *

#rec = Record(InterfaceCMD)


class SpecifyAttrError(Exception):
    """"""


class RecordAttrs(Enum):
    """List of attributes for record of address book."""

    name = Name, str
    birthday = Birthday, str
    phone = Phone, list
    address = Address, list
    email = Email, list
    note = Note, list


class Record:
    """Input record datas from console"""

    def __init__(self, interface: object) -> None:
        self.interface = interface()
        for attr in RecordAttrs:
            if attr.value[1] == str:
                while not hasattr(self, attr.name):
                    input_msg = self.interface.get_msg(f"Enter value for the \"{attr.name}\"", attr.value[1])
                    if input_msg:
                        try:
                            setattr(self, attr.name, attr.value[0](input_msg))
                        except (InvalidBirthdayValue) as err_msg:
                            print(err_msg)
                    else:
                        break
            elif attr.value[1] == list:
                attr_values = []
                input_msg = self.interface.get_msg(f"Enter values for the \"{attr.name}\". Use ';' separator", attr.value[1])
                for item_attr in input_msg:
                    while not hasattr(self, attr.name):
                        try:
                            attr_values.append(attr.value[0](item_attr.strip()))
                            break
                        except (InvalidPhoneNumber, InvalidEmailAddress, InvalidNoteValue) as err_msg:
                            print(err_msg)
                            item_attr = self.interface.get_msg(f"Re-enter value for the \"{attr.name}\"", str)
                            if not item_attr:
                                break
                if attr_values:
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


class AddressBook(UserDict):
    """Add new instance of Record class in AddressBook"""

    def iterator(self, n: str = 1) -> List[str]:
        separator, enter = "="*60, "\n"
        yield from ([f"{separator}:{enter}{rec}" for name, \
            rec in list(self.items())[i: i + n]] for i in range(0, len(self), n))

    def add_record(self, interface: object) -> None:
        new_record = Record(interface)
        self.data[new_record.name.value] = new_record

    def save_data(self, filename: str) -> None:
        try:
            with open(filename, "wb") as fn:
                pickle.dump(self.data, fn)
            print(f"Saving to file \"{filename}\" is successful")
        except (FileNotFoundError, AttributeError, MemoryError):
            print(f"An error occurred while saving the file \"{filename}\"")

    def load_data(self, filename: str) -> None:
        try:
            with open(filename, 'rb') as fn:
                self.data = pickle.load(fn)
            print(f"Loading from file \"{filename}\" is successful")
        except (FileNotFoundError, AttributeError, MemoryError):
            print(f"An error occurred while opening the file \"{filename}\"")

    def show_commands(self) -> None:
        """Displaying commands with the ability to execute them"""

        option, index = pick(ManagerCommands.commands_desc, \
            f"Command name and description. Select command.\n{'='*60}", indicator="=>")
        print(f"You have chosen a command: {option}.\nLet's continue.\n{'='*60}")
        ManagerCommands.functions_list[index]()
    
    def add_record(self):
        """"""
    def edit_record(self):
        """"""
    def holidays_period(self):
        """"""
    def print_notes(self):
        """"""
    def add_note(self):
        """"""
    def edit_note(self):
        """"""
    def del_note(self):
        """"""
    def find_sort_note(self):
        """"""
    def add_tags(self):
        """"""
    def sort_files(self):
        """"""
    def find_contact(self):
        """"""
    def del_contact(self):
        """"""
    def show_contacts(self):
        """"""


book = AddressBook()

class ManagerCommands(Enum):

    title = "We have chosen several options from the command you provided.\nPlease choose the one that you need."
    exit_commands = ["exit", "goodby", "close"]
    action_commands = ["help", "add_contact", "edit_record", "holidays_period", "print_notes", "add_note", \
    "edit_note", "del_note", "find_note", "add_tag", "sort_files", "find_contact", "del_contact", "show_contacts"]
    description_commands = ["Display all commands", "Add user to the address book", \
    "Edit information for the specified user", "Amount of days where we are looking for birthdays", \
    "Show notes for the specified user", "Add notes to the specified user", "Edit the notes for the specified user", \
    "Delete the notes for the specified user", "Find notes for specified user", \
    "Add tag for the specified user", "Sorts files in the specified directory", \
    "Search for the specified user by name", "Delete the specified user", \
    "Show all contacts in address book", "Exit from program"]
    functions_list = [book.show_commands, book.add_record, book.edit_record, book.holidays_period, \
    book.print_notes, book.add_note, book.edit_note, book.del_note, book.find_sort_note, book.add_tags, \
    book.sort_files, book.find_contact, book.del_contact, book.show_contacts, exit]

    @classmethod
    @property
    def commands_func(self):
        return {cmd: func for cmd, func in zip(self.action_commands.value, self.functions_list.value)}

    @classmethod
    @property
    def commands_desc(self):
        action_exit_desc = zip(self.action_commands.value + [', '.join(self.exit_commands.value)], self.description_commands.value)
        len_action = len(max(self.action_commands.value, key=len))
        return [f"{cmd:<{len_action}} -  {desc}" for cmd, desc in action_exit_desc]


class CommandHandler:

    def __call__(self, command: str) -> bool:
        if command in ManagerCommands.exit_commands.value:
            return False
        elif command in ManagerCommands.action_commands.value:
            ManagerCommands.commands_func[command]()
            return True
        command = get_close_matches(command, ManagerCommands.action_commands.value + ManagerCommands.exit_commands.value)
        in_exit = not set(command).isdisjoint(ManagerCommands.exit_commands.value)
        if in_exit:
            return False
        in_action = not set(command).isdisjoint(ManagerCommands.action_commands.value)
        if in_action:
            if len(command) == 1:
                ManagerCommands.commands_func[command[0]]()
            elif len(command) > 1:
                command = pick(command, ManagerCommands.title.value, indicator="=>")[0]
                print(f"You have selected the {command} command")
                ManagerCommands.commands_func[command]()
        else:
            print("Sorry, I could not recognize this command!")
        return True

current_script_path = Path(__file__).absolute()
file_bin_name = f"{current_script_path.stem}.bin"
data_file = current_script_path.parent.joinpath(file_bin_name)
# book.add_record(InterfaceCMD)

def main():
    """get data file from current directory"""
    book.load_data(data_file)
    command = CommandHandler()
    input_msg = input("Hello, please enter the command:\n").lower().strip()
    while command(input_msg):
        input_msg = input("Please enter the command:\n").lower().strip()
    book.save_data(data_file)
    print("Have a nice day... Good bye!")

if __name__ == "__main__":
    main()
