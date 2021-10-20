def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# 0,1,1,2,3,5,8,13,21,34,[55] - результат 55
print(fibonacci(10))
