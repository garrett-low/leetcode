# Given an array of integers nums, you start with an initial positive value startValue.

# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

def min_start_value(nums):
    total = nums[0]
    lowest = total
    
    for i in range(1, len(nums)):
        total += nums[i]
        if total < lowest:
            lowest = total
    if lowest < 0:
        min_start = abs(lowest) + 1
    else:
        min_start = 1
    
    print(min_start)
    return min_start

min_start_value([-3,2,-3,4,2])
min_start_value([1,2])
min_start_value([1,-2,-3])
min_start_value([1,2])