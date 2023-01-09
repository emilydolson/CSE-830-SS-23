table = {}


def factorial(n):
    if n in table:
        return table[n]

    if n == 0:
        table[0] = 1
        return 1
    else:
        table[n] = n * factorial(n-1)
        return n * factorial(n-1)


print(factorial(10))