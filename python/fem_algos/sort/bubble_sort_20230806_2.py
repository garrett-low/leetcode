def bubble_sort(arr):
    last_unsorted = len(arr) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(last_unsorted):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
        last_unsorted -= 1
    print(arr)

bubble_sort([69, 420, 42, 55, 54, 10, 20, 30, 40, 9, 8])