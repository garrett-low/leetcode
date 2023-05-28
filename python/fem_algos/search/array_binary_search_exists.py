def binary_search_exist(array, number_to_find):
    
    return inner(array, number_to_find, 0, len(array) - 1)
    
def inner(array, number_to_find, start, end):
    if end < start:
        return False

    mid_index = (end + start)//2
    mid = array[mid_index]
    
    if mid == number_to_find:
        return True
    
    if mid < number_to_find:
        return inner(array, number_to_find, mid_index + 1, end)
    
    if mid > number_to_find:
        return inner(array, number_to_find, start, mid_index - 1)

# testing
test_array = []
for i in range(4):
    test_array.append(i)

print(test_array)
print("Find 0: ", binary_search_exist(test_array, 0))
print("Find 1: ", binary_search_exist(test_array, 1))
print("Find 2: ", binary_search_exist(test_array, 2))
print("Find 3: ", binary_search_exist(test_array, 3))
print("Find 4: ", binary_search_exist(test_array, 4))
print("Find 6: ", binary_search_exist(test_array, 6))