'''
Создайте класс NumberString наследуйте его от класса UserString,
определите для него метод number_count(self), который будет считать
количество цифр в строке.
'''
from collections import UserString

class NumberString(UserString):
    def number_count(self):
        print(self.data)
        return len([chr for chr in self.data if chr in '0123456789'])


nmbr = NumberString("2whoAre1You")
print(nmbr.number_count())
