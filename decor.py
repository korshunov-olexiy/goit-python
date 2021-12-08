import re
from difflib import get_close_matches

# from pick import pick


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


def get_input_msg(input_msg):
    result = {}

    def fill_result(input_msg, list_of_commands):
        for cmd in list_of_commands:
            spaces = len(cmd.split())
            msg = re.sub(r" +", " ", input_msg).split(" ", maxsplit=spaces)
            raw_cmd, raw_msg = ' '.join(msg[:spaces]), ' '.join(msg[spaces:])
            match = ''.join(get_close_matches(raw_cmd, [cmd]))
            if match:
                result.update({match: raw_msg})
    fill_result(input_msg, exit_commands)
    if not result:
        fill_result(input_msg, action_commands)
        len_res = len(result)
        if len_res == 0:
            print("Sorry, I could not recognize the entered command!")
            exit(0)
        elif len_res == 1:
            commands_func[cmd](input_str[len(cmd):].strip())
        else:
            title = 'Please select the command you want to execute or select "Cancel" to cancel the execution: '
            cmd, _ = pick(result, title, indicator="=>")
            commands_func[cmd](input_str[len(cmd):].strip())
    return result


def analize_input_msg(cmd_user):
    cmd_user = get_close_matches(cmd_user, action_commands + exit_commands)
    action_cmd = set(action_commands)
    exit_cmd = set(exit_commands)
    # если есть элемент из user_cmd в action_cmd возвращается False !!
    in_action = not cmd_user.isdisjoint(action_cmd)
    in_exit = not cmd_user.isdisjoint(exit_cmd)

    title = 'Please select the command you want to execute or select "Cancel" to cancel the execution: '
    options = cmd_user
    option, index = pick(options, title, indicator='=>')

    if in_exit and in_action:
        '''check action or exit'''
        print("Choice command:")
        commands_func.update({cmd_exit[0]: None})
        for one_cmd_user in cmd_user:
            '''run command choces user from menu'''
    elif in_exit and not in_action:
        '''exit program'''
    elif not in_exit and in_action:
        '''check what is action'''
    elif not in_exit and not in_action:
        '''print(not know command)'''


if __name__ == "__main__":
    address_book = {}
    action_commands = ['help', 'hello', 'add', 'change', 'phone', 'show all']
    functions_list = [cmd_help, cmd_hello, cmd_add, cmd_change, cmd_phone, cmd_show_all]
    commands_func = {cmd: func for cmd, func in zip(action_commands, functions_list)}
    exit_commands = ['good bye', 'close', 'exit']
    print(get_input_msg("hely   067 -431-23-15"))
