def mirage(filename):
    histories_list = [] # each item is one history - a list of lists
    with open(filename, 'rt') as file:
        for line in file:
            history = [int(x) for x in line.strip().split()]
            histories_list.append(history)
    
    print(histories_list)
    
    # P1
    next_val_list = []
    for history in histories_list:
        next_val = recursive_find_next_val(history)

def recursive_find_next_val(array):
    # base case
    is_diff_all_zero = True
    for diff in array:
        if diff != 0:
            is_diff_all_zero = False
    
    if is_diff_all_zero:
        return
    
    diff_list = []
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        diff_list.append(diff)
    print(diff_list)
                

mirage('sample.txt')