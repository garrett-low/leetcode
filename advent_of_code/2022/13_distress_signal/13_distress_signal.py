import ast
#
def distress_signal(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        idx = 0
        left = []
        right = []
        for line in file:
            idx += 1
            if line == '\n':
                continue
            line = line.strip()
            x = ast.literal_eval(line)
            if idx % 2 == 0:
                left.append(x)
            else:
                right.append(x)
    
    ret_sum = 0
    for pair_num in range(1, len(left) + 1, 1):
        is_correct_order = compare(left[pair_num], right[pair_num])
        if is_correct_order:
            ret_sum += pair_num
    
    print(ret_sum)
    return

def compare(left, right):
    if 

def test_eval():
    x = eval('[1,[2,[3,[4,[5,6,0]]]],8,9]')
    print(x)
    
    for item in x:
        print(item)

# test_eval()
distress_signal('sample.txt')