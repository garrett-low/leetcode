def encoding_error(filename, len_preamble):
    num_series = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            num_series.append(int(line.strip()))
    
    preamble_set = set(num_series[0:len_preamble])
    print(num_series)
    print(preamble_set)
    
    for i in range(len_preamble, len(num_series)):
        curr_target = num_series[i]
        found_pair = []
        if not is_valid_twosum(preamble_set, curr_target, found_pair):
            print(curr_target)
            return curr_target
        else:
            preamble_set.remove(num_series[i - len_preamble])
            preamble_set.add(curr_target)
    
    print("No invalid number found!")

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