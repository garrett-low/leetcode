def index_of(array, number_to_find):
    for i in range(len(array)):
        if array[i] == number_to_find:
            return i
    return -1


test_array = [1, 2, 3, 4]
print(test_array)
print("index of 1: ", index_of(test_array, 1))
print("index of 2: ", index_of(test_array, 2))
print("index of 3: ", index_of(test_array, 3))
print("index of 4: ", index_of(test_array, 4))
print("index of 5, returns -1 if DNE: ", index_of(test_array, 5))
