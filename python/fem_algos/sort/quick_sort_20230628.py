def qs(arr):
    qs_inner(arr, 0, len(arr) - 1)
    print(arr)
    return

def qs_inner(arr, lo, hi):
    if lo < 0 or lo >= hi:
        return
    
    pivot_idx = partition(arr, lo, hi)
    
    qs_inner(arr, lo, pivot_idx - 1)
    qs_inner(arr, pivot_idx + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    
    pivot_idx = lo - 1
    for i in range(lo, hi):
        if pivot > arr[i]:
            pivot_idx += 1
            temp = arr[pivot_idx]
            arr[pivot_idx] = arr[i]
            arr[i] = temp
    
    pivot_idx += 1
    arr[hi] = arr[pivot_idx]
    arr[pivot_idx] = pivot
    
    return pivot_idx

qs([420, 69, 350, 1, 10, 99])

# forgot base case and return pivot idx