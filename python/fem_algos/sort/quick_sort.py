# Lomuto partition scheme

def quick_sort(array):
    inner(array, 0, len(array) - 1)
    
    return array

def inner(array, low, high):
    if low >= high or low < 0:
        return
    
    pivot_index = partition(array, low, high)
    
    inner(array, low, pivot_index - 1)
    inner(array, pivot_index + 1, high)

def partition(array, low, high):
    pivot = array[high]
    pivot_index = low - 1
    for i in range(low, high, 1):
        if array[i] < pivot:
            pivot_index += 1
            swap(array, i, pivot_index)
    
    pivot_index += 1
    swap(array, pivot_index, high)
    return pivot_index

def swap(array, this_index, that_index):
    temp = array[this_index]
    array[this_index] = array[that_index]
    array[that_index] = temp
    
def main():
    array = [4, 3, 1, 7, 6, 2, 5]
    print(quick_sort(array))
    
    array2 = [420, 69, 42069, 1, 55, 123, 999]
    print(quick_sort(array2))
    
if __name__ == "__main__":
    main()