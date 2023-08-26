from collections import defaultdict

def acc_before_infinite(filename):
    op_list = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            line_split = line.strip().split(' ')
            op = line_split[0]
            val = int(line_split[1])
            op_list.append((op, val))
    
    acc = 0
    i = 0
    line_exec_ct = defaultdict(int)
    # P2
    op_list_with_prev = {}
    last_op_i = None
    prev = (op_list[0][0], op_list[0][1], i)
    while i < len(op_list):
        op, val = op_list[i]
        op_list_with_prev[i] = prev # p2
        
        line_exec_ct[i] += 1
        if line_exec_ct[i] >= 2:
            last_op_i = i # p2
            break
        
        prev = (op, val, i) # p2
        if op == 'acc':
            acc += val
            i += 1
        elif op == 'jmp':
            i += val
        elif op == 'nop':
            i += 1
    
    print(f"P1 acc before first repeat: {acc}")
    
    max_i = 0
    seen = set()
    while last_op_i and last_op_i not in seen:
        seen.add(last_op_i)
        op, val, prev_i = op_list_with_prev[last_op_i]
        # print(op, val, prev)
        if prev_i > max_i:
            max_i = prev_i
        last_op_i = prev_i
    # print(max_i)
    tmp_op, tmp_val = op_list[max_i]
    
    if tmp_op == 'jmp':
        tmp_op = 'nop'
    elif tmp_op == 'nop':
        tmp_op = 'jmp'
    
    op_list[max_i] = (tmp_op, tmp_val)
    # print((tmp_op, tmp_val))
    
    #p2 redo
    acc = 0
    i = 0
    line_exec_ct = defaultdict(int)
    while i < len(op_list):
        op, val = op_list[i]
        # print(op, val)
        
        # line_exec_ct[i] += 1
        # if line_exec_ct[i] >= 2:
            # break
        
        if op == 'acc':
            acc += val
            i += 1
        elif op == 'jmp':
            i += val
        elif op == 'nop':
            i += 1
    
    print("P2: ", acc)
    
acc_before_infinite('sample.txt')
# acc_before_infinite('input.txt')

# p2 first attempt 1287

# def test():
    # print(int('+4'))
    # print(int('-4'))
    # test_dict = defaultdict(int)
    # print(test_dict[0])
# test()