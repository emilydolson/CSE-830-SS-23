import math

def change(amt, num_coins, denom_list):
    if amt == 0:
        return 0
    # subtract the largest possible value out of the amount
    # calculate previous amount
    result = math.inf
    for i in range(num_coins):
        if denom_list[i] <= amt:
            new_amt = amt - denom_list[i]
            result_for_this_coin = change(new_amt, num_coins, denom_list)
            if result_for_this_coin + 1 < result:
                result = result_for_this_coin + 1
    return result
    

denom_list = [1, 3, 6, 12, 24, 30]
num_coins = len(denom_list)
amt = 48
# 50 = 24 24 1 1
# 49 = 24 24 1
# 48 = 24 24
# 48 - 30 = 18
# 47 = 30 12 3 1 1
# 35 = 30 3 1 1 
# 17 = 12 3 1 1

print(change(amt, num_coins, denom_list))