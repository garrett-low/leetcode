# has duplicate using an O(n*logn) sorting algorithm

def hasDuplicate(arr):
    print("unsorted: ", arr)
    qsort(arr, 0, len(arr) - 1)
    print("sorted: ", arr)
    
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            print("Has duplicate!")
            return True
    print("No duplicate!")
    return False

def qsort(arr, lo, hi):
    if lo < 0 or lo >= hi:
        return
    
    p_i = partition(arr, lo, hi)
    
    qsort(arr, p_i + 1, hi)
    qsort(arr, lo, p_i - 1)

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

hasDuplicate([1, 2, 9, 3, 5, 6, 8, 7, 0])
hasDuplicate([9, 2, 9, 3, 5, 6, 8, 7, 0])