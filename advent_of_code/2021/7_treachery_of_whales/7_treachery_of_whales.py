import ast

def find_median(filename):
    ary = []
    with open(filename, 'rt', encoding='utf-8') as file:
        input_str = '[' + file.readline().strip() + ']'
        ary = ast.literal_eval(input_str)
    qs(ary)
#     print(ary)
#     print(len(ary))
#     print(len(ary)//2)
    
    if len(ary) % 2 == 0:
        median = (ary[(len(ary)//2) - 1] + ary[(len(ary)//2)]) // 2
    else:
        median = ary[len(ary)//2]
    print(median)
    
    retval = 0
    for i in range(len(ary)):
        retval += abs(ary[i] - median)
    print(retval)

def qs(ary):
    qs_inner(ary, 0, len(ary) - 1)
    return ary

def qs_inner(ary, lo, hi):
    if lo >= hi or lo < 0:
        return
    p = pivot(ary, lo, hi)
    qs_inner(ary, p + 1, hi)
    qs_inner(ary, lo, p - 1)

def pivot(ary, lo, hi):
    p = ary[hi]
    
    p_idx = lo - 1
    for i in range(lo, hi):
        if ary[i] < p:
            p_idx += 1
            temp = ary[i]
            ary[i] = ary[p_idx]
            ary[p_idx] = temp
    
    p_idx += 1
    ary[hi] = ary[p_idx]
    ary[p_idx] = p
    return p_idx

find_median("sample.txt")
find_median("input.txt")