def bs_index_of(arr, num):
    return inner(arr, num, 0, len(arr) - 1)

def inner(arr, num, start, end):
    if end < start:
        return -1
    
    mid_idx = (start + end) // 2
    mid = arr[mid_idx]
    
    if num == mid:
        return mid_idx
    
    if mid < num:
        return inner(arr, num, mid_idx + 1, end)
    
    if mid > num:
        return inner(arr, num, start, mid_idx - 1)
    
# testing
test_array = []
for i in range(5):
    test_array.append(i)

print(test_array)
print("Find 0: ", bs_index_of(test_array, 0))
print("Find 1: ", bs_index_of(test_array, 1))
print("Find 2: ", bs_index_of(test_array, 2))
print("Find 3: ", bs_index_of(test_array, 3))
print("Find 4: ", bs_index_of(test_array, 4))
print("Find 5: ", bs_index_of(test_array, 5))
print("Find 6: ", bs_index_of(test_array, 6))