# --*-- coding: utf-8 --*--

def input_error(func):
    def check_error(input_str):
        if func.__name__ == "get_input_command":
            result = func(input_error)
            return result
        elif func.__name__ in ['cmd_hello', 'cmd_show_all']:
            result = func()
            return result
        try:
            result = func
            return result
        except KeyError as err_key:
            print(err_key)
        except ValueError as err_val:
            print(err_val)
        except IndexError as err_idx:
            print(err_idx)

@input_error
def cmd_hello():
    msg = "How can I help you?"
    return msg

@input_error
def cmd_add(input_str):
    name, phone = input_str.split()
    address_book[name.strip().capitalize()] = phone.strip()
    return f"User {name} with phone number {phone} has been added to address book"

@input_error
def cmd_change(input_str):
    name, phone = input_str.split()
    address_book[name.strip().capitalize()] = phone.strip()
    return f"The phone number for {name} has been changed"

@input_error
def cmd_phone(input_str):
    name = input_str.split().capitalize()
    finding_phone = address_book.get(name)
    if finding_phone:
        return f"The {name} has a phone number as {finding_phone}"
    else:
        return "This user was not found in the database"

@input_error
def cmd_show_all():
    res = []
    for user_info in address_book:
        name, phone = user_info.items()
        res.append(f"{name}: {phone}")
    return '\n'.join(res)

address_book = []
commands_list = ['hello', 'add', 'change', 'phone', 'show_all']
functions_list = [cmd_hello, cmd_add, cmd_change, cmd_phone, cmd_show_all]
commands_func = {cmd: func for cmd, func in zip(commands_list, functions_list)}

def get_handler(operator):
    return commands_func[operator]

def get_input_command(input_str):
    cmd = ''.join([c for c in commands_list if input_msg.startswith(c)])
    if cmd:
        print(get_handler(cmd)(input_msg))
    else:
        print("Sorry, I could not recognize the entered command!")

if __name__ == "__main__":
    input_msg = input("Hello, please enter one of the commands: hello, add, change, phone or show all\n: ").lower().strip()
    while input_msg != ['good bye', 'close', 'exit']:
        get_input_command(input_msg)
        input_msg = input("Hello, please enter one of the commands: hello, add, change, phone or show all\n: ").lower().strip()
    
    print("Have a nice day... Good bye!")
