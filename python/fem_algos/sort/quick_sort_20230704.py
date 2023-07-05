def qs(arr):
    qs_inner(arr, 0, len(arr) - 1)
    print(arr)
    return

def qs_inner(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    
    pivot = partition(arr, lo, hi)
    
    qs_inner(arr, pivot + 1, hi)
    qs_inner(arr, lo, pivot - 1)

def partition(arr, lo, hi):
    piv = arr[hi]
    
    piv_idx = lo - 1
    for i in range(lo, hi):
        if arr[i] < piv:
            piv_idx += 1
            temp = arr[i]
            arr[i] = arr[piv_idx]
            arr[piv_idx] = temp
    
    piv_idx += 1
    arr[hi] = arr[piv_idx]
    arr[piv_idx] = piv
    return piv_idx

qs([420, 59, 69, 1, 5, 3, 2, 42069])

# forgot to set initial pivot index to low - 1
# I set it to -1 instead of low - 1