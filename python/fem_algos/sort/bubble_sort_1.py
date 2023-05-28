def bubble(arr):
    last_unsorted = len(arr)
    while last_unsorted > 0:
        for i in range(0, len(arr) - 1, 1): #len-1 because i and i+1
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        
        last_unsorted -= 1
    
    return arr

# test
arr1 = [1, 3, 7, 4, 2]
print(arr1)
print(bubble(arr1))