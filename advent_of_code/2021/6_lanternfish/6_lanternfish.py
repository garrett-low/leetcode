import ast

def spawn(filename, num_days):
    ary = []
    with open(filename, 'rt', encoding='utf-8') as file:
        input_str = '[' + file.readline().strip() + ']'
        ary = ast.literal_eval(input_str)
    
    print(ary)
    for _ in range(num_days):
        start_len = len(ary) # don't decrement new fish
        for i in range(start_len):
            if ary[i] == 0:
                ary.append(8)
                ary[i] = 6
            else:
                ary[i] -= 1
#         print(ary)
    
    print(len(ary))

spawn('sample.txt', 1)
# spawn('input.txt', 80)