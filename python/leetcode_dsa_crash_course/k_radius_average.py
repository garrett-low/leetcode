def k_radi_avg(nums, k):
    if k == 0:
        print(nums)
        return nums
    
    output = [-1] * len(nums)
    
    if (2 * k + 1) > len(nums):
        return output
    
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])
    
    # for i in range(k - 1):
        # output.append(-1)
    
    # for i in range(k - 1, len(nums) - k):
        # curr_sum = prefix[i + k] - prefix[i - k]
        # curr_avg = curr_sum // (2 * k + 1)
        # output.append(curr_avg)
    
    # for i in range(len(nums) - k, len(nums)):
        # output.append(-1)
    
    for i in range(k, len(nums) - k):
        # if i - k < 0 or i > (len(nums) - k - 1):
            # output.append(-1)
            # continue
        
        left_sum = 0
        if i - k > 0:
            left_sum = prefix[i - k - 1]
        curr_sum = prefix[i + k] - left_sum
        curr_avg = curr_sum // (2 * k + 1)
        output[i] = curr_avg
    
    print(output)
    return output

k_radi_avg([7,4,3,9,1,8,5,2,6], 3)
k_radi_avg([100000], 0)
k_radi_avg([8], 10000)