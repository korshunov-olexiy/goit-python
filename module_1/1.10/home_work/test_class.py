from collections import UserDict, UserList


class Name:
    def __init__(self, name):
        self.value = name

class Phone:
    def __init__(self, phones):
        if isinstance(phones, str):
            self.values = [p.replace(' ', '') for p in phones.split(',')]
        else:
            self.values = [p.replace(' ', '') for p in phones]

class Record(UserDict):
    def __init__(self, name, phones = []):
        self.data = {'name': Name(name), 'phones': Phone(phones)}


john = Record('John', '23-23-121, 2-234-2-34-2')
bob = Record('Bob', ['123-345-2351', '24-456-234-976'])

print(john['name'].value)
print(bob['phones'].values)
