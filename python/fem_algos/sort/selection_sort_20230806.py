import sys

def selection_sort(arr):
    first_unsorted_i = 0
    while first_unsorted_i <= len(arr) - 1:
        min = sys.maxsize
        min_i = -1
        for i in range(first_unsorted_i, len(arr)):
            if arr[i] < min:
                min_i = i
                min = arr[i]
        arr[min_i], arr[first_unsorted_i] = arr[first_unsorted_i], arr[min_i]
        first_unsorted_i += 1
    print(arr)

selection_sort([69, 420, 42, 55, 54, 10, 20, 30, 40, 9, 8])