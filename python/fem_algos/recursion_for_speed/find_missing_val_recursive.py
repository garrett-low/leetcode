# The following function finds the “missing number” from an array of inte-
# gers. That is, the array is expected to have all integers from 0 up to the
# array’s length, but one is missing. As examples, the array, [5, 2, 4, 1, 0] is
# missing the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the
# number 8.
# Here’s an implementation that is O(N2) (the includes method alone is already
# O(N), since the computer needs to search the entire array to find n):
# function findMissingNumber(array) {
#   for(let i = 0; i < array.length; i++) {
#       if(!array.includes(i)) {
#           return i;
#       }
#   }
#
#   // If all numbers are present:
#   return null;
# }
# Use sorting to write a new implementation of this function that only takes
# O(N log N). (There are even faster implementations, but we’re focusing on
# using sorting as a technique to make code faster.)

def find_missing(arr):
    sorted = merge_sort(arr)
    
    for i in range(len(sorted) - 1):
        if sorted[i] + 1 != sorted[i + 1]:
            print("missing: ", sorted[i] + 1)
            return sorted[i] + 1
    
    print("no numbers missing!")
    return None

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    arr_left = merge_sort(arr[:mid])
    arr_right = merge_sort(arr[mid:])
    
    return merge(arr_left, arr_right)

def merge(arr_left, arr_right):
    sorted = []
    i = 0
    j = 0
    
    while i < len(arr_left) and j < len(arr_right):
        left = arr_left[i]
        right = arr_right[j]
        
        if left < right:
            sorted.append(left)
            i += 1
        else:
            sorted.append(right)
            j += 1
    
    sorted.extend(arr_left[i:])
    sorted.extend(arr_right[j:])
    
    return sorted

find_missing([5, 2, 4, 1, 0])
find_missing([9, 3, 2, 5, 6, 7, 1, 0, 4])
find_missing([9, 3, 2, 5, 6, 7, 1, 0, 4, 8])