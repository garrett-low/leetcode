# quick select

def quick_select(arr, nth_highest):
    arr_copy = arr.copy()
    nth_value = qs(arr_copy, nth_highest, 0, len(arr_copy) - 1)
    print(nth_value)

def qs(arr, nth_highest, low, high):
    if high <= low:
        return arr[low]
        
    pivot_i = partition(arr, low, high)
    
    if pivot_i == nth_highest:
        return arr[pivot_i]
    elif nth_highest > pivot_i:
        return qs(arr, nth_highest, pivot_i + 1, high)
    else:
        return qs(arr, nth_highest, low, pivot_i - 1)

def partition(arr, low, high):
    pivot_val = arr[high]
    
    pivot_i = low - 1
    for i in range(low,high):
        if arr[i] < pivot_val:
            pivot_i += 1
            temp = arr[i]
            arr[i] = arr[pivot_i]
            arr[pivot_i] = temp
    
    pivot_i += 1
    arr[high] = arr[pivot_i]
    arr[pivot_i] = pivot_val
    return pivot_i

quick_select([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
quick_select([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)
quick_select([3, 7, 8, 2, 4, 9, 1, 5, 6], 3)
quick_select([3, 7, 8, 2, 4, 9, 1, 5, 6], 0)
quick_select([3, 7, 8, 2, 4, 9, 1, 5, 6], 8)