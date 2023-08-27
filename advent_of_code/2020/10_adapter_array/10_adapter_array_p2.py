from collections import defaultdict

BUILT_IN_JOLT_DIFFERENCE = 3
MAX_JOLT_DIFFERENCE = 3

def adapter_array(filename):
    adapters = [0]
    max_adapter = 0
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            adapter = int(line.strip())
            adapters.append(adapter)
            if adapter > max_adapter:
                max_adapter = adapter
    # built-in adapter
    built_in_adapter = max_adapter + BUILT_IN_JOLT_DIFFERENCE
    adapters.append(built_in_adapter)
    
    qsort(adapters, 0, len(adapters) - 1)
    # print(adapters)
    
    adapter_groups = []
    prev = 0
    curr = 0
    group = []
    for i in range(len(adapters)):
        prev = curr
        curr = adapters[i]
        
        if curr >= prev + MAX_JOLT_DIFFERENCE:
            adapter_groups.append(group)
            group = []
            start_group_val = curr
        
        group.append(curr)

    adapter_groups.append(group)
    
    print(adapter_groups)
    
    ct_combos = 1
    # this is not robust
    # the input only has contiguous groups of up to length 5
    # there are also no 2-jolt gaps
    for group in adapter_groups:
        if len(group) == 4:
            ct_combos *= 4
        elif len(group) == 3:
            ct_combos *= 2
        elif len(group) == 5:
            ct_combos *= 7
    
    print(f"P2:\t{ct_combos}")

def qsort(arr, lo, hi):
    if lo < 0 or lo >= hi:
        return arr
    pivot_i = partition(arr, lo, hi)
    
    qsort(arr, pivot_i + 1, hi)
    qsort(arr, lo, pivot_i - 1)

def partition(arr, lo, hi):
    pivot_val = arr[hi]
    
    pivot_i = lo - 1
    for i in range(lo, hi):
        if arr[i] < pivot_val:
            pivot_i += 1
            temp = arr[i]
            arr[i] = arr[pivot_i]
            arr[pivot_i] = temp
    
    pivot_i += 1
    arr[hi] = arr[pivot_i]
    arr[pivot_i] = pivot_val
    return pivot_i

def descend(adapters):
    return join_adapter(adapters, i - 3, i) + join_adapter(adapters, i - 2, i) + join_adapter(adapters, i - 1, i)

def join_adapter(adapters, i, j):
    if adapters[i] <= adapters[j] + 3:
        return 1
    return 0

    curr = len(adapters) - 1
    if adapters[curr] - adapters[curr - 1] == 3:
        curr = curr - 1
    elif adapters[curr] - adapters[curr - 1] == 2:
        pass
    elif adapters[curr] - adapters[curr - 1] == 1:
        pass


adapter_array('sample.txt')
adapter_array('sample2.txt')
adapter_array('input.txt')