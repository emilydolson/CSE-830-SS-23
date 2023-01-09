# Simplest case: 0! = 1
# Recurrence relationship: n! = n * (n-1)!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def factorial_math(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

for i in range(10):
    print(i, factorial(i), factorial_math(i))