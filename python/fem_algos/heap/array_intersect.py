# Common-sense guide to DSA: Chapter 8 - Exercise 1

def intersect(arr1, arr2):
    check_set = set(arr1)
    intersect_set = set()
    
    for test_item in arr2:
        if test_item in check_set:
            intersect_set.add(test_item)
    
    print(intersect_set)

intersect([350, 1, 2, 3, 4, 5, 420, 69], [0, 420, 2, 4, 6, 69, 8])