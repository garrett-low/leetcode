def qs(arr):
    qs_inner(arr, 0, len(arr) - 1)
    print(arr)
    return

def qs_inner(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    
    pivot = partition(arr, lo, hi)
    
    qs_inner(arr, lo, pivot - 1)
    qs_inner(arr, pivot + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    
    new_pivot = lo - 1
    for i in range(lo, hi):
        if arr[i] < pivot:
            new_pivot += 1
            temp = arr[i]
            arr[i] = arr[new_pivot]
            arr[new_pivot] = temp
    
    new_pivot += 1
    arr[hi] = arr[new_pivot]
    arr[new_pivot] = pivot
    return new_pivot

qs([420, 69, 350, 1234, 234, 34, 99, 5])

# forgot return new pivot index
# forgot base case
# forgot new pivot starts at (lo - 1) not (-1)