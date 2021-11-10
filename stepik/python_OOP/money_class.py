class Money:
    def __init__(self,dollars,cents):
        self.__dollars = dollars
        self.__cents = cents
        self.total_cents = (self.dollars*100)+self.cents
    @property
    def dollars(self):
        return self.__dollars
    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.__dollars = value
            self.total_cents = (self.dollars*100)+self.cents
        else:
            print("Error dollars")
    @property
    def cents(self):
        return self.__cents
    @cents.setter
    def cents(self,value):
        if isinstance(value, int) and 100 > value >= 0:
            self.__cents = value
            self.total_cents = (self.dollars*100)+self.cents
        else:
            print("Error cents")
    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 6666
print(Bill.total_cents)
print( list(Bill.__dict__.keys()) == ['total_cents'] )
# print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
# Bill.cents = 12
# print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
# print(Bill.total_cents)
