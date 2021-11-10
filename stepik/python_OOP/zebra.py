'''Создайте класс Zebra, внутри которого есть метод which_stripe,
который поочередно печатает фразы "Полоска белая", "Полоска черная",
начиная именно с фразы "Полоска белая"'''
class Zebra:
    def __init__(self):
        self.stripe = True
    def which_stripe(self):
        print("Полоска белая" if self.stripe else  "Полоска черная")
        self.stripe = not self.stripe

z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
