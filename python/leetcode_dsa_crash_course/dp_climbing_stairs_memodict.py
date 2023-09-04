# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# from collections import defaultdict
from collections import defaultdict

def stairs(n):
    memo = defaultdict(int)
    num_paths = count_paths(n, memo)
    print(num_paths)
    return num_paths

def count_paths(n, memo):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    print("hello")
    memo[n] = count_paths(n - 1, memo) + count_paths(n - 2, memo)
    return memo[n]

stairs(2)
stairs(3)