import timeit

a = "hi"

def test_global():
    b = "hi"
    a + a

def test_local():
    b = "hi"
    b + b

print("Globals", timeit.timeit(test_global, number = 1000000))
print("Locals", timeit.timeit(test_local,   number = 1000000))
