# Common-Sense DSA: Chapter 11
# Count the number of x's in input string

def countx(input):
    count = countx_inner(input, 0)
    print(count)

def countx_inner(input, i):
    if i >= len(input):
        return 0
    
    retval = 0
    if input[i].lower() == 'x':
        retval = 1
    
    return retval + countx_inner(input, i + 1)

countx('axbxcxdxex')