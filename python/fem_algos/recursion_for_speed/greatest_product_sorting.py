# Given an array of positive numbers, write a function that returns the
# greatest product of any three numbers. The approach of using three
# nested loops would clock in at O(N3), which is very slow. Use sorting to
# implement the function in a way that it computes at O(N log N) speed.
# (There are even faster implementations, but we’re focusing on using
# sorting as a technique to make code faster.)

def max_product(arr):
    print("unsorted: ", arr)
    sorted = merge_sort(arr)
    print("sorted: ", sorted)
    
    print(sorted[0] * sorted[1] * sorted[2])
    return sorted[0] * sorted[1] * sorted[2]

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
        left = arr_left[i]
        right = arr_right[j]
        
        if left < right:
            sorted.append(right)
            j += 1
        else:
            sorted.append(left)
            i += 1
    
    sorted.extend(arr_left[i:])
    sorted.extend(arr_right[j:])
    
    return sorted

max_product([5, 8, 9, 3, 7, 4, 6, 2, 10, 1])
max_product([5, 8, 9, 10, 7, 4, 5, 1, 3, 6, 2, 10, 1, 0, 10])