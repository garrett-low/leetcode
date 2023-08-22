# Write three different implementations of a function that finds the greatest
# number within an array. Write one function that is O(N2), one that is O(N
# log N), and one that is O(N)

def get_max_n2(arr):
    found_max = False
    for i in range(len(arr)):
        found_max = True
        for j in range(len(arr)):
            if i == j:
                continue
            
            if arr[j] > arr[i]:
                found_max = False
                break
        
        if found_max:
            print("max: ", arr[i])
            return arr[i]

get_max_n2([5, 8, 9, 3, 7, 4, 6, 2, 10, 1])

def get_max_nlogn(arr):
    sorted = merge_sort(arr)
    
    print("max: ", sorted[0])

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

get_max_nlogn([0, 99, 420, 69, 350, 999, 100, 1, 3, 4, 8, 7, 5, 2, 9])

def get_max_n(arr):
    max = -1
    
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    
    print("max: ", max)

get_max_n([350, 420, 99, 6969, 69, 5, 100, 123, 234, 9999])