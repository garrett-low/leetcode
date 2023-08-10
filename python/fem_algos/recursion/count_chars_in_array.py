# common-sense DSA chapter 11 exercises
# count chars in array of strings

def count_chars(input):
    count = count_inner(input, 0)
    print(count)

def count_inner(input, i):
    if i >= len(input):
        return 0
    # if type(input[i]) is str:
    count = len(input[i])
    
    return count_inner(input, i + 1) + count
    
count_chars(["ab", "c", "def", "ghij"])
count_chars(["ab", "c", "def", "ghij", "klmnop"])