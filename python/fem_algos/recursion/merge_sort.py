# merge sort

def ms(arr):
    sorted = merge_sort(arr)
    print(sorted)

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid_i = len(arr) // 2
    arr_left = merge_sort(arr[:mid_i])
    arr_right = merge_sort(arr[mid_i:])
    
    return merge(arr_left, arr_right)

def merge(arr_left, arr_right):
    sorted = []
    i = 0
    j = 0
    
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] < arr_right[j]:
            sorted.append(arr_left[i])
            i += 1
        else:
            sorted.append(arr_right[j])
            j += 1
    
    sorted.extend(arr_left[i:])
    sorted.extend(arr_right[j:])
    
    return sorted

ms([520, 420, 69, 350, 210, 9, 8, 7, 1, 2, 4, 9999])