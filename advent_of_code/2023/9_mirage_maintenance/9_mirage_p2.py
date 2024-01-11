def mirage(filename):
    histories_list = [] # each item is one history - a list of lists
    with open(filename, 'rt') as file:
        for line in file:
            history = [int(x) for x in line.strip().split()]
            histories_list.append(history)
    
    # print(histories_list)
    
    # P1
    first_val_list = []
    for history in histories_list:
        first_val = recursive_find_first_val(history)
        first_val_list.append(first_val)
    # print(first_val_list)
    print(histories_list)

    sum = 0
    for first_val in first_val_list:
        sum += first_val
    print(sum)

def recursive_find_first_val(array):
    # base case
    is_diff_all_zero = True
    for diff in array:
        if diff != 0:
            is_diff_all_zero = False
    
    if is_diff_all_zero:
        return 0 
    
    diff_list = []
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        diff_list.append(diff)
    # print(diff_list)
    
    recursive_find_first_val(diff_list)

    first_val = diff_list[0]
    first_val_parent = array[0]
    array.insert(0, first_val_parent - first_val)
    return array[0]

mirage('sample.txt') # P2: 2
mirage('input.txt') # P2: 993 
