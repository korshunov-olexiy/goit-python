def discount_price(discount):
    def inner(price):
        return price * (1 - discount)

    return inner


# example
price = 100
cost_15 = discount_price(0.15)
print(cost_15(price))
