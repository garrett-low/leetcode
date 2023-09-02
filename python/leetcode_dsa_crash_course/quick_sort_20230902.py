def qs_out(arr):
    print(arr)
    qs(arr, 0, len(arr) - 1)
    print(arr)

def qs(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    pivot_i = partition(arr, lo, hi)
    
    qs(arr, pivot_i + 1, hi)
    qs(arr, lo, pivot_i - 1)

def partition(arr, lo, hi):
    pivot_val = arr[hi]
    
    pivot_i = lo - 1
    for i in range(lo, hi):
        if arr[i] < pivot_val:
            pivot_i += 1
            arr[i], arr[pivot_i] = arr[pivot_i], arr[i]
    
    pivot_i += 1
    arr[hi] = arr[pivot_i]
    arr[pivot_i] = pivot_val
    return pivot_i

qs_out([420, 69, 35, 999, 3, 4, 7, 1])