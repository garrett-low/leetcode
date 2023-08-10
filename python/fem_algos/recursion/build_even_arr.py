# Common-sense guide to DSA: Chapter 11
# Takes an array of ints and returns an array of even ints

def build_even(src_arr):
    dest_arr = []
    dest_arr = even_inner(src_arr, 0)
    print(dest_arr)

def even_inner(src_arr, i):
    out_arr = []
    if i >= len(src_arr):
        return []
    if src_arr[i] % 2 == 0:
        return [src_arr[i]]
    
    return out_arr + even_inner(src_arr, i + 1)

build_even([1, 2, 3, 4, 5, 69, 420, 350])