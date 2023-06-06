# supply stacks part 2

def supply():
    line_count_to_moves = 0
    initial_state = []
    num_stacks = 0
    
    with open('input.txt', 'rt', encoding='utf-8') as file:
        for line in file:
            initial_state.append(line)
            line_count_to_moves += 1
            if line.isspace():
                break
        
        list_of_stacks = set_initial_state(initial_state)
        
        for line in file:
            split_line = line.split(' ')
            num_moves = int(split_line[1])
            stack_from = int(split_line[3]) - 1
            stack_to = int(split_line[5]) - 1
            
            index_start_move = len(list_of_stacks[stack_from]) - num_moves
            
            move_list = list_of_stacks[stack_from][index_start_move : ]
#             print(f"{move_list}")
            
            list_of_stacks[stack_to].extend(move_list)
            
            for i in range(int(num_moves)):
                pop_last(list_of_stacks[stack_from])
    
    # debug
    for i in range(len(list_of_stacks)):
        print(f"{list_of_stacks[i]}")
        
    for i in range(len(list_of_stacks)):
        print(f"{list_of_stacks[i][len(list_of_stacks[i]) - 1]}", end = '')

def pop_last(stack):
    return stack.pop(len(stack) - 1)

def set_initial_state(initial_state):
    num_stacks = count_stacks(initial_state)
    stack_indices = find_stack_indices(initial_state)
    print(f"{stack_indices}")
    list_of_stacks = [[] for i in range(num_stacks)]
    
    for i in range(len(initial_state) - 3, -1, -1):
        row = initial_state[i]

        stack_num = 0
        for stack_index in stack_indices:
            crate_val = row[stack_index]
            if not crate_val.isspace():
                list_of_stacks[stack_num].append(crate_val)
            stack_num += 1
    
    # debug
#     for i in range(len(list_of_stacks)):
#         print(f"{list_of_stacks[i]}")
    
    return list_of_stacks

def count_stacks(initial_state):
    stack_label_line = initial_state[len(initial_state) - 2].strip()
    last_label_index = stack_label_line.rfind(' ')
    last_label = int(stack_label_line[(last_label_index + 1) : ])
    return last_label

def find_stack_indices(initial_state):
    stack_indices = []
    stack_label_line = initial_state[len(initial_state) - 2]
    for i in range(len(stack_label_line)):
        val = stack_label_line[i]
        if not val.isspace():
            stack_indices.append(i)
            
    return stack_indices

supply()
