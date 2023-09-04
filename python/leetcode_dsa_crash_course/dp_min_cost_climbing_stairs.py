# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

from functools import cache

def min_cost(cost):
    @cache
    def dp(i):
        if i <= 1:
            return 0
        
        return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
    
    answer = dp(len(cost))
    print(answer)
    return answer

min_cost([10,15,20])
min_cost([1,100,1,1,1,100,1,1,100,1])