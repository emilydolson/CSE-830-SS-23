import timeit
import random

class BadHashObj():
    def __init__(self, my_val):
        self.value = my_val
    def __hash__(self):
        return self.value % 2

class GoodHashObj():
    def __init__(self, my_val):
        self.value = my_val
    def __hash__(self):
        return hash(self.value)

def use_bad_hash_obj():
    BadHashObj(random.randint(1,1000)) in bad_hash_dict

def use_good_hash_obj():
    GoodHashObj(random.randint(1,1000)) in good_hash_dict


print("n, good, bad")
for n in range(0, 100000, 10000):
    bad_hash_dict = {}
    for i in range(n):
        bad_hash_dict[BadHashObj(random.randint(1, 1000))] = 1

    good_hash_dict = {}
    for i in range(n):
        good_hash_dict[GoodHashObj(random.randint(1, 1000))] = 1


    bad_time = timeit.timeit(use_bad_hash_obj, number=1000)
    good_time = timeit.timeit(use_good_hash_obj, number=1000)
    print(",".join([str(n), str(good_time), str(bad_time)]))
