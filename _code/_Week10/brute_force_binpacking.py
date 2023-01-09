import random

best = 0

def binpack(items, capacity, current_solution):

    global best

    if sum(current_solution) > capacity:
        return 0

    if sum(current_solution) + sum(items) <= best:
        return 0

    if len(items) == 0:
        result = sum(current_solution)
        if result > best:
            best = result
        return sum(current_solution)

    curr_item = items.pop()
    included = binpack(items[:], capacity, current_solution + [curr_item])
    excluded = binpack(items[:], capacity, current_solution)

    return max(included, excluded)


#capacity = int(input())
#items = [float(i) for i in input().split(" ")]

capacity = 10
#items = [3.3, 7.2, 6, 3.1, 3.3, 2.1, 2.3, 1.1, 2, 1, 0.2, 1, .2, .3, .4, .5, .6, .7, .8, .9, 3.2, 2.7, 1.1, .6, .7, .8, .9, 3.2, 2.7, 1.1, 10]
random.seed(1)
items = [random.random() for i in range(22)]

items.sort()

print(binpack(items, capacity, []))




