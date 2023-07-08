def qs(arr):
    qs_inner(arr, 0, len(arr) - 1)
    print(arr)
    return

def qs_inner(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    
    pivot_idx = partition(arr, lo, hi)
    qs_inner(arr, lo, pivot_idx - 1)
    qs_inner(arr, pivot_idx + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    pivot_idx = lo - 1
    
    for i in range(lo, hi):
        if arr[i] < pivot:
            pivot_idx += 1
            temp = arr[pivot_idx]
            arr[pivot_idx] = arr[i]
            arr[i] = temp
    
    pivot_idx += 1
    arr[hi] = arr[pivot_idx]
    arr[pivot_idx] = pivot
    return pivot_idx

qs([1, 2, 3, 4, 5, 6])

qs([9, 8, 7, 6, 5, 4])

qs([5, 3, 9, 6, 7, 1])