# https://www.reddit.com/r/adventofcode/comments/k8zd1j/2020_day_8_is_there_a_non_brute_force_solution/gf304uf/
# A colleague pointed out the following algorithm, which is O(n) in time and space.
# Basically, it's a simple recursion, with the key point that the seen[...] array is NOT reset 
# when backtracking. 
# Thus, every program instruction is visited at most once (no matter how the recursion branches), 
# so it's O(n).
# // Pseudocode:
# seen[*] = false
# terminates(index, accumulator, can_swap):
    # if index == len(program):
        # print accumulator
        # return true
    # if seen[index]:
        # return false
    # seen[index] = true
    # new_index, new_accumulator = execute_instruction(index, accumulator)
    # if terminates(new_index, new_accumulator, can_swap):
        # return true
    # if can_swap AND program[index] is a jmp or nop:
        # swap the instruction at program[index] (i.e., jmp -> nop, or nop -> jmp)
        # new_index, new_accumulator = execute_instruction(index, accumulator)
        # if terminates(new_index, new_accumulator, false):
            # return true
    # return false

# // Call it like so:
# terminates(0, 0, true)

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
    is_finished, accumulator = exec_with_swap(op_list, visited_set, path, False, 0, 0)
    print(accumulator)
    
    # debug
    for tuple in path:
        step_i, op, val, accumulator, swapped = tuple
        print(f"{step_i}:\t{op}\t{val}\t{accumulator}\t{swapped}")

def exec_with_swap(op_list, visited_set, path, step_i, has_swapped, accumulator):
    if step_i == len(op_list):
        # print(f"Fin:\t\t\t{accumulator}")
        path.append((step_i, None, None, accumulator, ""))
        return True, accumulator
    
    if step_i in visited_set:
        return False, 0
    
    visited_set.add(step_i)
    op, val = op_list[step_i]
    # print(f"{step_i}:\t{op}\t{val}\t{accumulator}")
    path.append((step_i, op, val, accumulator, ""))
    new_step_i, new_accumulator = exec_op(op, val, step_i, accumulator)
    is_finished, final_accumulator = exec_with_swap(op_list, visited_set, path, new_step_i, has_swapped, new_accumulator)
    if is_finished:
        return True, final_accumulator
    path.pop()
    
    # didn't return True, try swap
    if has_swapped:
        return False, 0
    
    if op == 'nop' or op == 'jmp':
        if op == 'nop':
            op = 'jmp'
        else:
            op = 'nop'
        
        path.append((step_i, op, val, accumulator, "SWAPPED!!!"))
        new_step_i, new_accumulator = exec_op(op, val, step_i, accumulator)
        is_finished, final_accumulator = exec_with_swap(op_list, visited_set, path, new_step_i, True, new_accumulator)
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