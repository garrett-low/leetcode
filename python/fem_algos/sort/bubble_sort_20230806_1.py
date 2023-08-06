def bubble_sort(arr):
    last_unsorted = len(arr) - 1
    while last_unsorted > 0:
        for i in range(last_unsorted):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        last_unsorted -= 1
    print(arr)
    
bubble_sort([69, 420, 42, 55, 54, 10, 20, 30, 40, 9, 8])