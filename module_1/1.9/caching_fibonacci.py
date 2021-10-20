# функция с кешем, если уже считалось значение выдать результат, если нет посчитать
def caching_fibonacci():
    cache = {0:0,1:1}
    def fibonacci(n):
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci


print(caching_fibonacci()(153))
