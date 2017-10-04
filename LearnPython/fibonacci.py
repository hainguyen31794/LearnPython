
# from functools import lru_cache
dic = {}


def fibonacci(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    dic[n] = value
    return value


for i in range(1, 500):
    print fibonacci(i)
