#06/01/2023

def quick_sort(array):
    qs_inner(array, 0, len(array) - 1)
    
    return array

def qs_inner(array, low, high):
    if low >= high or low < 0:
        return
    
    pivot_index = partition(array, low, high)
    
    qs_inner(array, pivot_index + 1, high)
    qs_inner(array, low, pivot_index - 1)
    
def partition(array, low, high):
    pivot_val = array[high]
    
    new_pivot_index = low - 1
    for i in range(low, high):
        if array[i] < pivot_val:
            new_pivot_index += 1
            temp = array[new_pivot_index]
            array[new_pivot_index] = array[i]
            array[i] = temp
    
    new_pivot_index += 1
    array[high] = array[new_pivot_index]
    array[new_pivot_index] = pivot_val
    return new_pivot_index
    
def main():
    array = [4, 3, 1, 7, 6, 2, 5]
    print(quick_sort(array))
    
    array2 = [420, 69, 42069, 1, 55, 123, 999]
    print(quick_sort(array2))
    
if __name__ == "__main__":
    main()