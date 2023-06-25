import ast
#
def distress_signal(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        idx = 0
        packets = []
        for line in file:
            if line == '\n':
                continue
            line = line.strip()
            x = ast.literal_eval(line)
            packets.append(line)    
#     for packet in packets:
#         print(packet)
#     return
    
    ret_sum = 0
    pair_num = 1
    debug_ret_list = []
    for i in range(len(left)):
#         print(f"pair {pair_num}: {left[i]} vs {right[i]}")
        is_correct_order = unwrap_and_compare(left[i], right[i], 1)
#         print(f"{is_correct_order}\n")
        if is_correct_order:
            ret_sum += pair_num # pair_num is 0-based
            debug_ret_list.append(pair_num)
        pair_num += 1
    
    print(debug_ret_list)
    print(ret_sum)
    return

def unwrap_and_compare(left, right, indent):
    if isinstance(left, int) and isinstance(right, int):
        print(indent * "    " + f"- {left} vs. {right}")
        if left < right: # correct order
            return True
        elif right < left: # incorrect order
            return False
        else: # third case for equality
            return None
    
    if isinstance(left, int) and isinstance(right, list):
        return unwrap_and_compare([left], right, indent + 1)
    if isinstance(left, list) and isinstance(right, int):
        return unwrap_and_compare(left, [right], indent + 1)
    
    if isinstance(left, list) and isinstance(right, list):
        print(indent * "    " + f"- {left} vs. {right}")
        left_len = len(left)
        right_len = len(right)
        if left_len >= right_len:
            loop_num = right_len
        else:
            loop_num = left_len
            
        for i in range(loop_num):
            result = unwrap_and_compare(left[i], right[i], indent + 1)
            if result == True:
                return True
            elif result == False:
                return False
        
#         return left_len <= right_len
        if left_len < right_len:
            return True
        elif right_len < left_len:
            return False
        
        return None
    
    print ("debug - this should be unreachable!")
    return False

def test_eval():
    x = eval('[1,[2,[3,[4,[5,6,0]]]],8,9]')
    print(x)
    
    for item in x:
        print(item)
    
    print(type(x))
    if isinstance(x, list):
        print("x is a list, yes!")
    else:
        print("NAHHH")
    
    if isinstance(x[0], int):
        print("x is an int!")
    else:
        print("NAHHH")

def quick_sort(arr):
    qs(arr, 0, len(arr) - 1)
    
    print(arr)
    return arr

def qs(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    pivot_idx = weak_sort(arr, lo, hi)
    
    qs(arr, lo, pivot_idx - 1)
    qs(arr, pivot_idx + 1, hi)
    
def weak_sort(arr, lo, hi):
    pivot = arr[hi]
    
    pivot_idx = lo - 1
    for i in range(lo, hi):
        if arr[i] < pivot:
            pivot_idx += 1
            temp = arr[pivot_idx]
            arr[pivot_idx] = arr[i]
            arr[i] = temp
    
    pivot_idx += 1
    arr[hi] = arr[pivot_idx]
    arr[pivot_idx] = pivot
    return pivot_idx

# test_eval()
# distress_signal('sample.txt')
# distress_signal('input.txt')
# distress_signal('empty_compare.txt')

quick_sort([420, 69, 1, 2, 3, 90, 52, 100, 99])
