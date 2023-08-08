# Common-Sense DSA: Chapter 11

def arr_sum(arr):
    arr_sum_blah = arr_sum_inner(arr, 0)
    print(arr_sum_blah)

def arr_sum_inner(arr, i):
    if i >= len(arr):
        return 0
    
    return arr[i] +  arr_sum_inner(arr, i + 1)

arr_sum([1, 2, 3, 4])