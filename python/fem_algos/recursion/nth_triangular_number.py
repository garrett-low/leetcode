# Common-Sense DSA: Chapter 11
# Return nth number in triangular number series

def triangular_num(n):
    nth_num = tri_inner(n)
    print(f"{n}: {nth_num}")

def tri_inner(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + tri_inner(n - 1)

triangular_num(7)
triangular_num(6)

def tri_nums(n):
    tri_num_list = []
    tri_list_inner(n, tri_num_list)
    print(f"{n}: {tri_num_list}")

def tri_list_inner(n, tri_num_list):
    curr = 0
    if n == 0:
        # don't append anything
        return 0
    if n == 1:
        tri_num_list.append(1)
        return 1
    
    curr += n + tri_list_inner(n - 1, tri_num_list)
    tri_num_list.append(curr)
    return curr

tri_nums(7)
tri_nums(6)
tri_nums(1)
tri_nums(0)