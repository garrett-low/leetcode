def max_subarray(nums):
    curr_subarray = [nums[0]]
    curr_subarray_sum = nums[0]
    max_subarray_sum = curr_subarray_sum
    max_subarray = curr_subarray
    
    for i in range(1, len(nums)):
        curr = nums[i]
        curr_subarray_sum += curr
        curr_subarray.append(curr)
        if curr_subarray_sum < curr:
            curr_subarray_sum = curr
            curr_subarray = [curr]
        if curr_subarray_sum > max_subarray_sum:
            max_subarray = curr_subarray
            max_subarray_sum = curr_subarray_sum
    
    print(max_subarray)
    print(max_subarray_sum)
    return max_subarray_sum

max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
max_subarray([5,4,-1,7,8])
max_subarray([1])