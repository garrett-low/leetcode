# Common-sense guide to DSA: Chapter 8 - Exercise 2

def first_duplicate(arr):
    arr_set = set()
    for test_item in arr:
        if test_item in arr_set:
            print(test_item)
            return test_item
        else:
            arr_set.add(test_item)

first_duplicate(['a', 'b', 'c', 'd', 'e', 'c', 'f'])