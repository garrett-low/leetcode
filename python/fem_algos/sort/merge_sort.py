def ms(arr):
    print(arr)
    sorted_arr = merge_sort(arr)
    print(sorted_arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    arr_left = merge_sort(arr[:mid])
    arr_right = merge_sort(arr[mid:])
    
    return merge(arr_left, arr_right)

def merge(arr_left, arr_right):
    sorted_arr = []
    i = 0
    j = 0
    
    while i < len(arr_left) and j < len(arr_right):
        left = arr_left[i]
        right = arr_right[j]
        if left < right:
            sorted_arr.append(left)
            i += 1
        else:
            sorted_arr.append(right)
            j += 1
    
    sorted_arr.extend(arr_left[i:])
    sorted_arr.extend(arr_right[j:])
    
    return sorted_arr

ms([420, 350, 690, 6969, 9, 8, 1, 2, 3, 99, 5, 55, 6, 7, 10])