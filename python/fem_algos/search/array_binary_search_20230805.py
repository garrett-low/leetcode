def bin_search(arr, target):
	found = bs(arr, target, 0, len(arr) - 1)
	print(found)
	
def bs(arr, target, lo, hi):
    if lo > hi:
        return -1
    mid_i = (lo + hi) // 2
    mid = arr[mid_i]

    if mid == target:
        return mid_i	
    elif mid < target:
        return bs(arr, target, mid_i + 1, hi)
    else:
        return bs(arr, target, lo, mid_i - 1)

bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)