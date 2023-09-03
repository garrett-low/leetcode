# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
from collections import defaultdict

def largest_unique(nums):
    freq_nums = defaultdict(int)
    
    for num in nums:
        freq_nums[num] += 1
    
    max_num = -1
    for num in freq_nums:
        if freq_nums[num] > 1:
            continue
        
        if num > max_num:
            max_num = num
    
    print(max_num)
    return max_num

largest_unique([5,7,3,9,4,9,8,3,1])
largest_unique([9,9,8,8])