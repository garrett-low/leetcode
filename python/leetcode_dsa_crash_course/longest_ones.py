def longest_ones(nums, k):
    start = 0
    curr_zeros = 0
    max_len = 0
    
    for i in range(len(nums)):
        curr = nums[i]
        if curr == 0:
            curr_zeros += 1
            if curr_zeros > k:
                # remove 0 from left
                while nums[start] != 0 and start < len(nums):
                    start += 1
                start += 1
                curr_zeros -= 1
        
        curr_len = i - start + 1
        
        if curr_len > max_len:
            max_len = curr_len
    
    print(max_len)
    return max_len

longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2)
longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)