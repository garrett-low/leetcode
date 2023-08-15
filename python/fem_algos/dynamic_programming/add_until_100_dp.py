# The following function accepts an array of numbers and returns the sum,
# as long as a particular number doesn’t bring the sum above 100. If adding
# a particular number will make the sum higher than 100, that number is
# ignored. However, this function makes unnecessary recursive calls. Fix
# the code to eliminate the unnecessary recursion:

# I would never write it this way in the first place, but this is how the book
# wrote it as an example.
# It also adds the array in reverse (last index first)...?
def add_100_non_dp(arr):
    output = add_until_100_non_dp(arr, 0)
    print(output)

def add_until_100_non_dp(arr, i):
    if i >= len(arr):
        return 0
    if arr[i] + add_until_100_non_dp(arr, i + 1) > 100:
        return add_until_100_non_dp(arr, i + 1)
    else:
        return arr[i] + add_until_100_non_dp(arr, i + 1)

add_100_non_dp([30, 33, 28, 29, 27, 26])

def add_100(arr):
    output = add_100_inner(arr, 0, 0)
    print(output)

def add_100_inner(arr, i, curr_sum):
    if i >= len(arr):
        return curr_sum
    
    if curr_sum + arr[i] < 100:
        curr_sum += arr[i]
    
    curr_sum = add_100_inner(arr, i + 1, curr_sum)
    return curr_sum
    
add_100([30, 33, 28, 29, 27, 26])