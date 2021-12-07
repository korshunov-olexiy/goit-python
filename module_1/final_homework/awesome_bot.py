# --*-- coding: utf-8 --*--


def input_error(func):
    """Decorator for error handling.
    
    Args:
    func - Decorated function."""
    def check_error(input_str):
        # If we perform the functions cmd_help, cmd_hello, cmd_show_all,
        # they do not require parameters.
        if func.__name__ in ['cmd_help', 'cmd_hello', 'cmd_show_all']:
            return func()
        try:
            return func(input_str)
        except KeyError as err_key:
            return err_key
        except ValueError as err_val:
            return err_val
        except IndexError as err_idx:
            return err_idx
    return check_error


@input_error
def cmd_help():
    """Gives a list of commands that the bot understands."""
    return f"Sorry, the bot understands the following commands: {', '.join(commands_list[:-1])} and {commands_list[-1]}"


@input_error
def cmd_hello():
    """Gives a welcome message to the console."""
    return "How can I help you?"


@input_error
def cmd_add(input_str):
    """Save the user name and phone number entered in address_book.
    
    Args:
    input_str - Input string from a user without a passed command."""
    name, phone = input_str.split()
    address_book[name.strip().capitalize()] = phone.strip()
    return f"User {name} with phone number {phone} has been added to address book"


@input_error
def cmd_change(input_str):
    """Change the transmitted phone number of the specified user.
    
    Args:
    input_str - Input string from a user without a passed command."""
    name, phone = input_str.split()
    address_book[name.strip().capitalize()] = phone.strip()
    return f"The phone number for {name} has been changed to {phone}"


@input_error
def cmd_phone(input_str):
    """Find a user by name in the database.

    Args:
    input_str - Input string from a user without a passed command."""
    name = input_str.capitalize()
    finding_phone = address_book.get(name)
    if finding_phone:
        return f"The {name} has a phone number as {finding_phone}"
    else:
        return "This user was not found in the database"


@input_error
def cmd_show_all():
    """Show all records from the database."""
    return "\n".join(f"{k}: {v}" for k, v in address_book.items())


@input_error
def get_input_command(input_str):
    """Attempts to find a command in the passed line

    Args:
    input_str - Input string from a user without a passed command."""
    cmd = ''.join([c for c in commands_list if input_str.startswith(c)])
    if cmd:
        print(commands_func[cmd](input_str[len(cmd):].strip()))
    else:
        print("Sorry, I could not recognize the entered command!")


if __name__ == "__main__":

    address_book = {}
    # List of commands.
    commands_list = ['help', 'hello', 'add', 'change', 'phone', 'show all']
    # List of functions
    functions_list = [cmd_help, cmd_hello, cmd_add, cmd_change, cmd_phone, cmd_show_all]
    # Dictionary of combined lists of commands and functions.
    commands_func = {cmd: func for cmd, func in zip(commands_list, functions_list)}

    input_msg = input("Hello, please enter the command: ").lower().strip()
    while input_msg not in ['good bye', 'close', 'exit']:
        get_input_command(input_msg)
        input_msg = input("Please enter the command: ").lower().strip()
    
    print("Have a nice day... Good bye!")

