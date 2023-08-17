# quick sort

def quick_sort(arr):
    qs(arr, 0, len(arr) - 1)
    
    print(arr)

def qs(arr, lo, hi):
    if lo < 0 or lo >= hi:
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
            temp = arr[i]
            arr[i] = arr[pivot_i]
            arr[pivot_i] = temp
    
    pivot_i += 1
    arr[hi] = arr[pivot_i]
    arr[pivot_i] = pivot_val
    return pivot_i

quick_sort([69, 420, 350, 1, 9, 8, 7, 3, 4, 5])