# Common-Sense DSA: Chapter 11
# Find first index with x in string
# Assume string has at least one x

def find_x(input):
    first_x_i = find_x_inner(input, 0)
    print(first_x_i)
    
def find_x_inner(input, i):
    if i >= len(input):
        print("not found!")
        return -1
    
    if input[i] == 'x':
        return i
    
    return find_x_inner(input, i + 1)

find_x("abcdefghijklmnopqrstuvwxyz")
find_x("xxx")
find_x("01234x")