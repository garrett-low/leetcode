# https://www.codewars.com/kata/57403b5ad67e87b5e7000d1d/

def bubble(arr):
    arr_of_arr = []
    #arr_of_arr.append(arr.copy())
    
    last_unsorted = len(arr)
    while last_unsorted > 0:
        for i in range(0, len(arr) - 1, 1): #len-1 because i and i+1
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                arr_of_arr.append(arr.copy())
        
        last_unsorted -= 1
    
    return arr_of_arr