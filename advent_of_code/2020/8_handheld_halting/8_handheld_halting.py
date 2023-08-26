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
    while i < len(op_list):
        op, val = op_list[i]
        
        line_exec_ct[i] += 1
        if line_exec_ct[i] >= 2:
            break
        
        if op == 'acc':
            acc += val
            i += 1
        elif op == 'jmp':
            i += val
        elif op == 'nop':
            i += 1
    
    print(f"P1 acc before first repeat: {acc}")
    
acc_before_infinite('sample.txt')
acc_before_infinite('input.txt')

# def test():
    # print(int('+4'))
    # print(int('-4'))
    # test_dict = defaultdict(int)
    # print(test_dict[0])
# test()