# Middle Squares implementation
class MiddleSquare():
    # constructor
    def __init__(self, seed):
        self.seed = seed

    # random number call
    def get_rand(self):
        self.seed *= self.seed 
        self.seed = (self.seed // 1000) % 1000000
        return self.seed 


# Linear Congruential Generator
class LCG():
    # constructor
    def __init__(self, seed):
        self.seed = seed
        self.a = 21
        self.c = 91
        self.m = 10000000

    # random number call
    def get_rand(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

def repeat_time(rng):
    seen = set()
    count = 0

    while rng.seed not in seen:
        seen.add(rng.seed)
        rng.get_rand()
        count += 1
    
    return count

def main():
    # middle squares
    ms_rng = MiddleSquare(1265489751425469)
    print("Middle squares:")
    print(ms_rng.get_rand())
    print(ms_rng.get_rand())
    print(ms_rng.get_rand())
    print(ms_rng.get_rand())
    print("Time to repeat: ", repeat_time(ms_rng))

    # lcg
    lcg_rng = LCG(1265489751425469)
    print("LCG: ")
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print("Time to repeat: ", repeat_time(lcg_rng))

if __name__ == "__main__":
    main()