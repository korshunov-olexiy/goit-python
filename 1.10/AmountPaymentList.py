'''
Перепишем задачу расчета задолженностей по коммунальным услугам
с помощью класса UserList.
У нас есть список показаний задолженностей по коммунальным услугам
в конце месяца — список payment. Задолженности могут быть отрицательными
— у нас переплата или положительными, если необходимо оплатить по счетам.
Создайте класс AmountPaymentList наследуйте его от класса UserList.
Сделайте функцию amount_payment методом класса LookUpKeyDict.
'''
from collections import UserList
from functools import reduce

class AmountPaymentList(UserList):
    def amount_payment(self):
        return reduce(lambda x, y: x + y if y >= 0 else x, self.data, 0)


# EXAMPLE:
payment = AmountPaymentList([1, -3, 4, -5, 10])
print(payment.amount_payment())
