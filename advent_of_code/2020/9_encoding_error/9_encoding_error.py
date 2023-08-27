import sys

def encoding_error(filename, len_preamble):
    num_series = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            num_series.append(int(line.strip()))
    
    preamble_set = set(num_series[0:len_preamble])
    # print(num_series)
    # print(preamble_set)
    
    invalid_num = None
    for i in range(len_preamble, len(num_series)):
        curr_target = num_series[i]
        found_pair = []
        if not is_valid_twosum(preamble_set, curr_target, found_pair):
            print(f"P1:\t{curr_target}") # P1
            invalid_num = curr_target
            break
        else:
            preamble_set.remove(num_series[i - len_preamble])
            preamble_set.add(curr_target)
    
    if not invalid_num:
        print("No invalid number found!")
        return
    
    # P2
    start_i, end_i = find_subarray_sum(num_series, invalid_num)
    min_val, max_val = find_min_max(num_series, start_i, end_i)
    print(f"P2:\t{start_i}\t{end_i}\t{min_val}\t{max_val}\t{min_val + max_val}")

# P2
def find_min_max(num_series, start_i, end_i):
    min_val = sys.maxsize
    max_val = 0
    for i in range(start_i, end_i + 1):
        curr = num_series[i]
        if curr < min_val:
            min_val = curr
        if curr > max_val:
            max_val = curr
    
    return min_val, max_val

# P2 - find contiguous subarray that adds up to the target value
# using a left and right pointer
def find_subarray_sum(num_series, invalid_num):
    start_i = 0
    sliding_window_sum = 0
    for i in range(len(num_series)):
        sliding_window_sum += num_series[i]
        if sliding_window_sum == invalid_num:
            return start_i, i
        
        while sliding_window_sum > invalid_num:
            sliding_window_sum -= num_series[start_i]
            start_i += 1
            if sliding_window_sum == invalid_num:
                return start_i, i
    
    print("No subarray found!")
    return None, None

# P1
def is_valid_twosum(preamble_set, curr_target, found_pair):
    # complement_dict = {}
    for num in preamble_set:
        complement = curr_target - num
        if complement in preamble_set:
            found_pair.append(num)
            found_pair.append(complement)
            return True
    
    return False

encoding_error('sample.txt', 5)
encoding_error('input.txt', 25)