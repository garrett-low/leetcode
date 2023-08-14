# quick sort

def qs(arr):
    qs_inner(arr, 0, len(arr) - 1)
    print(arr)

def qs_inner(arr, lo, hi):
    if lo < 0 or lo >= hi:
        return
    
    p_i = partition(arr, lo, hi)
    
    qs_inner(arr, p_i + 1, hi)
    qs_inner(arr, lo, p_i - 1)
    
    return

def partition(arr, lo, hi):
    p_val = arr[hi]
    
    p_i = lo - 1
    for i in range(lo, hi):
        if arr[i] < p_val:
            p_i += 1
            temp = arr[i]
            arr[i] = arr[p_i]
            arr[p_i] = temp
    
    p_i += 1
    arr[hi] = arr[p_i]
    arr[p_i] = p_val
    return p_i

qs([9, 8, 69, 420, 6, 7, 5, 4, 3, 2, 1])