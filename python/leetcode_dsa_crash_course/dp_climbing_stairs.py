# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# from collections import defaultdict
from functools import cache

def stairs(n):
    num_paths = count_paths(n)
    print(num_paths)
    return num_paths

@cache
def count_paths(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    print("hello")
    return count_paths(n - 1) + count_paths(n - 2)

stairs(2)
stairs(3)