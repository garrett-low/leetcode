# Find the max val in an array using dynamic programming

def find_max_non_dp(arr):
    max = find_max_non_dp_inner(arr, 0)
    print(max)

def find_max_non_dp_inner(arr, i):
    if i >= len(arr):
        return -1
    
    if arr[i] > find_max_non_dp_inner(arr, i + 1):
        return arr[i]
    else:
        return find_max_non_dp_inner(arr, i + 1)

find_max_non_dp([1,420, 69, 10, 350, 9999])

def find_max(arr):
    max_val = f_max(arr, 0)
    print(max_val)

def f_max(arr, i):
    if i >= len(arr):
        return -1
    
    max_subarr = f_max(arr, i + 1)
    
    if arr[i] > max_subarr:
        return arr[i]
    else:
        return max_subarr

find_max([9999, 350, 420, 69, 1, 999, 1000])