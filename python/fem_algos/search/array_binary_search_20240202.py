def array_bs(array, num):
    return inner(array, num, 0, len(arr) - 1)

def inner(array, num, start, end):
    if end < start:
        return -1
    
    mid_idx = (start + end) // 2
    mid = array[mid_idx]

    if num == mid:
        return mid_idx
    if mid < num:
        inner(
