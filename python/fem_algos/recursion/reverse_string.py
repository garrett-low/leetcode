# Common-Sense DSA: Chapter 11

def reverse_str(input):
    reverse_inner(input, 0)
    print()

def reverse_inner(input, i):
    if len(input) <= i:
        return
    
    reverse_inner(input,  i + 1)
    print(input[i], end='')

reverse_str('abcde')

def rev_str(input):
    reversed = rev_inner(input, 0)
    print(reversed)

def rev_inner(input, i):
    if i >= len(input):
        return ""
    
    return rev_inner(input, i + 1) + input[i]

rev_str('xyz')