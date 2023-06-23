import ast
import functools
#
def distress_signal(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        packets = []
        for line in file:
            if line == '\n':
                continue
            line = line.strip()
            packet = ast.literal_eval(line)
            packets.append(packet)
    
    divider_one = [[2]]
    divider_two = [[6]]
    packets.append(divider_one)
    packets.append(divider_two)
    
#     for packet in packets:
#         print(packet)
    
    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare))
    
#     for packet in sorted_packets:
#         print(packet)
    
    divider_one_idx = sorted_packets.index(divider_one)
    divider_two_idx = sorted_packets.index(divider_two)
    prod = (divider_one_idx + 1) * (divider_two_idx + 1)
    print(prod)
    
    return

def compare(left, right):
    result = unwrap_and_compare(left, right, 0)
#     print(result)
    if result == None:
        return 0
    elif result:
        return -1
    else:
        return 1

def unwrap_and_compare(left, right, indent):
    if isinstance(left, int) and isinstance(right, int):
#         print(indent * "    " + f"- {left} vs. {right}")
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
#         print(indent * "    " + f"- {left} vs. {right}")
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

# test_eval()
# distress_signal('sample.txt')
distress_signal('input.txt')
# distress_signal('empty_compare.txt')