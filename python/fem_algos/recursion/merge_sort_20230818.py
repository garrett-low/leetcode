# merge_sort

def merge_outer(arr):
    sorted = merge_sort(arr)
    print("sorted: ", sorted)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    arr_left = merge_sort(arr[:mid])
    arr_right = merge_sort(arr[mid:])
    
    return merge(arr_left, arr_right)

def merge(arr_left, arr_right):
    sorted = []
    i = 0
    j = 0
    
    while i < len(arr_left) and j < len(arr_right):
        left_val = arr_left[i]
        right_val = arr_right[j]
        if left_val < right_val:
            sorted.append(left_val)
            i += 1
        else:
            sorted.append(right_val)
            j += 1
    
    # add the remaining sub array
    sorted.extend(arr_left[i:])
    sorted.extend(arr_right[j:])
    
    return sorted

merge_outer([9, 8, 7, 6, 5, 4, 3, 2, 1])