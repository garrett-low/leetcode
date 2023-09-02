def missing_num(nums):
    num_set = set(nums)
    
    for i in range(len(nums) + 1):
        if i not in num_set:
            print(i)
            return i
    
    return -1

missing_num([3,0,1])
missing_num([0,1])