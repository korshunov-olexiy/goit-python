"""
1. Напишите классы сериализации контейнеров с данными Python в json, bin файлы. Сами классы должны соответствовать общему интерфейсу (абстрактному базовому классу) SerializationInterface.
2. Напишите класс метакласс Meta, который всем классам, для кого он будет метаклассом, устанавливает порядковый номер. Код для проверки правильности решения:
"""

from abc import ABCMeta, abstractclassmethod
from collections import UserDict
import pickle, json

# solve #2.1

class SerializationInterface(metaclass=ABCMeta):

    @abstractclassmethod
    def save_data(self, data: UserDict, filename: str) -> None:
        """ save_data abstract method """

    @abstractclassmethod
    def load_data(self, filename: str) -> UserDict:
        """load_data abstract method """


class SaveLoadBin(SerializationInterface):

    def save_data(self, data: UserDict, filename: str) -> None:
        with open(filename, "wb") as fn:
            pickle.dump(data, fn)

    def load_data(self, filename: str) -> UserDict:
        with open(filename, 'rb') as fn:
            return pickle.load(fn)

class SaveLoadJson(SerializationInterface):

    def save_data(self, data: UserDict, filename: str) -> None:
        with open(filename, "w") as fn:
            json.dump(data, fn)

    def load_data(self, filename: str) -> UserDict:
        with open(filename, "r") as fn:
            return json.load(fn)


# example of usage
saveload_bin = SaveLoadBin()
my_data = {"param1": 340, "param2": 341}
saveload_bin.save_data(my_data, "my_data.bin")
my_data = saveload_bin.load_data("my_data.bin")
print(my_data)


# solve #2.2

class Meta(type):
    children_number = 0
    def __new__(cls, name, bases, attrs):
        attrs["class_number"] = Meta.children_number
        Meta.children_number += 1
        return type.__new__(cls, name, bases, attrs)


Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data
        

class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
