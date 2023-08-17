# quick select

def quick_select(arr, nth_highest):
    arr_copy = arr.copy()
    nth_value = qs(arr_copy, nth_highest, 0, len(arr_copy) - 1)
    print(nth_value)

def qs(arr, nth_highest, low, high):
    pivot_i = partition(arr, low, high)
    if pivot_i == nth_highest:
        return arr[pivot_i]
    
        
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