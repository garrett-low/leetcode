import math

def sortedSquares(nums):
    square_sorted = []
    for i, val in enumerate(nums):
        if val >= 0:
            break
    
    right_i = i
    left_i = i - 1
    while right_i < len(nums) and left_i >= 0:
        right_val = nums[right_i]
        left_val = nums[left_i]
        if abs(right_val) < abs(left_val):
            square_sorted.append(right_val * right_val)
            right_i += 1
        else:
            square_sorted.append(left_val * left_val)
            left_i -= 1
    
    for i in range(right_i, len(nums)):
        square_sorted.append(nums[i] * nums[i])
    
    for j in range(left_i, -1, -1):
        square_sorted.append(nums[j] * nums[j])
    
    print(square_sorted)
    return square_sorted

sortedSquares([-7,-3,2,3,11])
sortedSquares([-4,-1,0,3,10])