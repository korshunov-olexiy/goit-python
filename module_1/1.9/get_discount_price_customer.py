'''
Функция принимает два параметра:
    price цена продукта
    customer словарь с данными клиента следующего вида: {"name": "Dima"} или {"name": "Boris", "discount": 0.15}
У вас есть глобальная переменная DEFAULT_DISCOUNT которая определяет скидку для клиента, если у него нет поля discount.
Функция get_discount_price_customer должна возвращать новую цену на товар для клиента.
Напомним, что дисконт discount это дробное число от 0 до 1. И мы под скидкой понимаем коэффициент,
который определяет размер от цены. И на этот размер мы понижаем итоговую цена товара: price = price * (1 - discount).
'''
DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if customer.get('discount', -1) != -1:
        print('test')
        return price * (1 - customer['discount'])
    else:
        return price * (1 - DEFAULT_DISCOUNT)

cust = {"name": "Dima"}
# cust = {"name": "Boris", "discount": 0.15}
# cust =  {'name': 'Olga', 'discount': 0}
print(get_discount_price_customer(10, cust))
