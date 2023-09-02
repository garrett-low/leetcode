def running_sum(nums):
    running = [nums[0]]
    
    for i in range(1, len(nums)):
        running.append(running[-1] + nums[i])
    
    print(running)
    return running

running_sum([1,2,3,4])
running_sum([1,1,1,1,1])
running_sum([3,1,2,10,1])