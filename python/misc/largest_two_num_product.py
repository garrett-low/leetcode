# You’re writing a function that accepts an array of numbers and computes
# the highest product of any two numbers in the array. At first glance, this
# is easy, as we can just find the two greatest numbers and multiply them.
# However, our array can contain negative numbers and look like this:
# [5, -10, -6, 9, 4]
# In this case, it’s actually the product of the two lowest numbers, -10 and
# -6 that yield the highest product of 60.
# We could use nested loops to multiply every possible pair of numbers,
# but this would take O(N2) time. Your job is to optimize the function so
# that it’s a speedy O(N).

import sys

def largest_two_product(arr):
    highest = 0
    highest_second = 0
    lowest = sys.maxsize
    lowest_second = sys.maxsize
    
    for num in arr:
        if num > highest:
            highest_second = highest
            highest = num
        elif num > highest_second:
            highest_second = num
        
        if num < lowest:
            lowest_second = lowest
            lowest = num
        elif num < lowest_second:
            lowest_second = num
    
    high_prod = highest * highest_second
    low_prod = lowest * lowest_second
    
    if high_prod > low_prod:
        print(high_prod)
    else:
        print(low_prod)

largest_two_product([5, -10, -6, 9, 4])
largest_two_product([-5, -4, -3, 0, 3, 4])
largest_two_product([-9, -2, -1, 2, 3, 7])
largest_two_product([-7, -4, -3, 0, 4, 6])
largest_two_product([-6, -5, -1, 2, 3, 9])
largest_two_product([-9, -4, -3, 0, 6, 7])