class NewInt(int):
    arg = None
    def __new__(cls, arg):
        cls.arg = arg
        return  super(NewInt, cls).__new__(cls, arg)
    def repeat(self,n=2):
        return int(str(self.arg)*n)
    def to_bin(self):
        return int(bin(self.arg)[2:])


a = NewInt(9)
print(99, a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(141414, d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(100011, b.to_bin()) # печатает 100011 - двоичное представление числа 35
print( NewInt(16).to_bin() )
