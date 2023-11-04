def bubble_sort(arr):
    last_unsorted = len(arr) - 1
    
    while last_unsorted > 0:
        for i in range(last_unsorted):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        last_unsorted -= 1
    
    print(arr)

bubble_sort([420,69,350,35,10,5,7,8,6,4,3,9,9,1,2])