def bs(arr):
    last_unsorted = len(arr) - 1
    while last_unsorted > 0:
        for i in range(0, last_unsorted):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
        last_unsorted -= 1
    print(arr)

bs([1, 2, 3, 4, 5, 6])
bs([6, 5, 4, 3, 2, 1])
bs([420, 350, 69, 999, 2, -1])