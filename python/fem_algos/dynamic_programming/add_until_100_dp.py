# The following function accepts an array of numbers and returns the sum,
# as long as a particular number doesn’t bring the sum above 100. If adding
# a particular number will make the sum higher than 100, that number is
# ignored. However, this function makes unnecessary recursive calls. Fix
# the code to eliminate the unnecessary recursion:

def add_until_100(arr):
    if len(arr) == 0:
        return 0
    