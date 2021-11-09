class Zebra:
    def __init(self):
        print(self)
        self.stripe = True
    def which_stripe(self):
        print("Полоска белая" if self.stripe else  "Полоска черная")
        self.stripe = not self.stripe

z1 = Zebra()
# print(z1.stripe)
# z1.which_stripe()
# z1.which_stripe()
# z1.which_stripe()
# z1.which_stripe()
# z1.which_stripe()
# z1.which_stripe()
