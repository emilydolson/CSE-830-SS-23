def knapsack_recur(weights, values, w):
    if w == 0:
        return 0, []
    
    if len(values) == 0:
        return 0, []

    included = float("-inf")
    incl_set = []
    curr = len(values) - 1
    if weights[curr] <= w:
        included, incl_set = knapsack_recur(weights[:curr], values[:curr], w - weights[curr])
        included += values[curr]
        incl_set += [curr]

    excluded, excl_set = knapsack_recur(weights[:curr], values[:curr], w)

    if included > excluded:
        return included, incl_set 
    else:
        return excluded, excl_set

    #return max(included, excluded)

def knapsack_dp(weights, values, w):
    table = [[0 for i in range(len(values) + 1)] for i in range(w+1)]

    for weight_i in range(1, w+1):
        for curr in range(1, len(values) + 1):
            included = float("-inf")
            if weights[curr-1] <= weight_i:
                included = table[weight_i - weights[curr - 1]][curr - 1] + values[curr - 1]

            excluded = table[weight_i][curr - 1]

            table[weight_i][curr] = max(included, excluded)

    return table[-1][-1]

weights = [2, 3, 1, 5, 3]
values = [40, 50, 100, 95, 30]
print(knapsack_recur(weights, values, 10))
print(knapsack_dp(weights, values, 10))