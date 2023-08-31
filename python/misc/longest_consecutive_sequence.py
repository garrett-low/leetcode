# You’re writing a function that accepts an array of unsorted integers and
# returns the length of the longest consecutive sequence among them. The
# sequence is formed by integers that increase by 1. For example, in the
# array:
# [10, 5, 12, 3, 55, 30, 4, 11, 2]
# the longest consecutive sequence is 2-3-4-5. These four integers form an
# increasing sequence because each integer is one greater than the previous
# one. While there’s also a sequence of 10-11-12, it’s only a sequence of
# three integers. In this case, the function should return 4, since that’s the
# length of the longest consecutive sequence that can be formed from this
# array.
# One more example:
# [19, 13, 15, 12, 18, 14, 17, 11]
# This array’s longest sequence is 11-12-13-14-15, so the function would
# return 5.
# If we sorted the array, we can then traverse the array just once to find
# the longest consecutive sequence. However, the sorting itself would take
# O(N log N). Your job is to optimize the function so that it takes O(N) time.

def longest_sequence(arr):
    test_set = set(arr)
    
    max_count = 0
    for num in arr:
        if num - 1 in test_set:
            continue
        
        curr_count = 0
        while num in test_set:
            curr_count += 1
            num += 1
        
        if curr_count > max_count:
            max_count = curr_count
    
    print(max_count)

longest_sequence([10, 5, 12, 3, 55, 30, 4, 11, 2])
longest_sequence([19, 13, 15, 12, 18, 14, 17, 11])