# Common-sense guide to DSA: Chapter 8 - Exercise 4
# Print first non-duplicated letter in input string
import sys

def nonduplicated(test_string):
    letter_count = {}
    for i in range(len(test_string)):
        char = test_string[i]
        if char in letter_count:
            idx, count = letter_count[char]
            count += 1
            letter_count[char] = (idx, count)
        else:
            letter_count[char] = (i, 1)
    
    min_i = sys.maxsize
    first_nonduplicated = ""
    for char in letter_count:
        i, count = letter_count[char]
        if i < min_i and count == 1:
            min_i = i
            first_nonduplicated = char
    
    print(first_nonduplicated)

nonduplicated('minimum')
nonduplicated('mississippi')
nonduplicated('maximum')
nonduplicated('conviction')