def merge_sort_out(arr):
    print(arr)
    sorted = merge_sort(arr)
    print(sorted)

def merge_sort(arr):
    if len(arr) == 1:
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
        left = arr_left[i]
        right = arr_right[j]
        if left < right:
            sorted.append(left)
            i += 1
        else:
            sorted.append(right)
            j += 1
    
    sorted.extend(arr_left[i:])
    sorted.extend(arr_right[j:])
    
    return sorted

merge_sort_out([420, 69, 35, 999, 3, 4, 7, 1])