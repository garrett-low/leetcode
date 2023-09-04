import sys

def coin_change(coins, amount):
    memo = [sys.maxsize] * (amount + 1)
    memo[0] = 0
    
    for curr_amt in range(1, amount + 1):
        for coin_denom in coins:
            if curr_amt - coin_denom >= 0:
                memo[curr_amt] = min(memo[curr_amt], 1 + memo[curr_amt - coin_denom])
    
    if memo[amount] == sys.maxsize:
        return -1
    
    print(memo[amount])
    return memo[amount]

coin_change([1,2,5], 11)