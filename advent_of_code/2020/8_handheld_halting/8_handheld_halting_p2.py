from collections import defaultdict

def handheld_halting_p2(filename):
    op_list = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            line_split = line.strip().split(' ')
            op = line_split[0]
            val = int(line_split[1])
            op_list.append((op, val))
    
    visited_set = set()
    path = []
    is_finished, accumulator = exec_with_swap(op_list, visited_set, path, 0, 0)
    print(accumulator)
    
    # debug
    for tuple in path:
        step_i, op, val, accumulator = tuple
        print(f"{step_i}:\t{op}\t{val}\t{accumulator}")

def exec_with_swap(op_list, visited_set, path, step_i, accumulator):
    if step_i == len(op_list):
        # print(f"Fin:\t\t\t{accumulator}")
        path.append((step_i, None, None, accumulator))
        return True, accumulator
    
    if step_i in visited_set:
        return False, 0
    
    visited_set.add(step_i)
    op, val = op_list[step_i]
    # print(f"{step_i}:\t{op}\t{val}\t{accumulator}")
    path.append((step_i, op, val, accumulator))
    new_step_i, new_accumulator = exec_op(op, val, step_i, accumulator)
    is_finished, final_accumulator = exec_with_swap(op_list, visited_set, path, new_step_i, new_accumulator)
    if is_finished:
        return True, final_accumulator
    path.pop()
    
    # didn't return True, try swap
    if op == 'nop' or op == 'jmp':
        if op == 'nop':
            op = 'jmp'
        else:
            op = 'nop'
        
        path.append((step_i, op, val, accumulator))
        new_step_i, new_accumulator = exec_op(op, val, step_i, accumulator)
        is_finished, final_accumulator = exec_with_swap(op_list, visited_set, path, new_step_i, new_accumulator)
        if is_finished:
            return True, final_accumulator
        path.pop()
    
    return False, 0
    
def exec_op(op, val, step_i, accumulator):     
    if op == 'acc':
        accumulator += val
        step_i += 1
    elif op == 'jmp':
        step_i += val
    elif op == 'nop':
        step_i += 1
    
    return step_i, accumulator

# handheld_halting_p2('sample.txt')
handheld_halting_p2('input.txt')

# p2 1287 too high
# 2512 too high