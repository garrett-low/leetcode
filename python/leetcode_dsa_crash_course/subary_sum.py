# Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
from collections import defaultdict

def subary_sum(nums, k):
    count_sums = defaultdict(int)
    count_sums[0] = 1
    output = 0
    curr_sum = 0
    
    for num in nums:
        curr_sum += num
        output += count_sums[curr_sum - k]
        count_sums[curr_sum] += 1
    
    print(output)
    return output

subary_sum([1, 2, 1, 2, 1], 3)