'''
Создайте класс LookUpKeyDict родителем которого будет класс UserDict.
Сделайте функцию lookup_key методом класса LookUpKeyDict
'''
from collections import UserDict

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys


# EXAMPLE:
d = LookUpKeyDict({1: 'a', 2: 'b', 3: 'c'})
print(d.lookup_key('b'))
