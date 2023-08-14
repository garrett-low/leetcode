# merge sort anagram

def swaps(str_start, str_fin):
    str_fin_dict = {}
    str_start = list(str_start)
    str_fin = list(str_fin)
    for i in range(len(str_fin)):
        str_fin_dict[str_fin[i]] = i
    print(str_fin_dict)
    
    str_out, ct_swaps = merge_sort(str_start, str_fin_dict)
    print(str_out)
    print(ct_swaps)

def merge_sort(str_start, str_fin_dict):
    ct_swaps = 0
    if len(str_start) <= 1:
        return str_start, ct_swaps
    
    mid_i = len(str_start) // 2
    arr_left, ct_left = merge_sort(str_start[:mid_i], str_fin_dict)
    arr_right, ct_right = merge_sort(str_start[mid_i:], str_fin_dict)
      
    sorted, ct_merge = merge(arr_left, arr_right, str_fin_dict)
    
    return sorted, ct_left + ct_right + ct_merge

def merge(arr_left, arr_right, str_fin_dict):
    i = 0
    j = 0
    ct_swaps = 0
    sorted = []
    
    while i < len(arr_left) and j < len(arr_right):
        left_char = arr_left[i]
        right_char = arr_right[j]
        if str_fin_dict[left_char] < str_fin_dict[right_char]:
            sorted.append(left_char)
            i += 1
        else:
            sorted.append(right_char)
            j += 1
            ct_swaps += 1
    
    sorted.extend(arr_left[i:])
    sorted.extend(arr_right[j:])
    
    return sorted, ct_swaps

swaps('sawp', 'swap')
swaps('listen', 'silent')