from collections import UserDict, UserList


print([d for d in dir(UserDict) if not d.startswith("_")])

class Record(UserDict):
    def __init__(self, name, phones = [], address = None):
        self.data = {'name': name}
        phones = [phones] if isinstance(phones, str) else phones
        self.data.update({'phones': phones})
        self.data.update({'address': address})


john = Record('John', '23-23-121')
bob = Record('Bob', ['123-345465-2351', '24-456-234-976'])

print(john)
print(bob)
