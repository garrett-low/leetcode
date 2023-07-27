def quick_sort(arr):
    qs(arr, 0, len(arr) - 1)
    print(arr)

def qs(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    
    p = pivot(arr, lo, hi)
    qs(arr, p + 1, hi)
    qs(arr, lo, p - 1)

def pivot(arr, lo, hi):
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

quick_sort([69, 420, 42069, 1234, 3, 4, 2, 1])