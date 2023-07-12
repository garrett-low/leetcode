import ast

def spawn(filename, num_days):
    ary = []
    with open(filename, 'rt', encoding='utf-8') as file:
        input_str = '[' + file.readline().strip() + ']'
        ary = ast.literal_eval(input_str)
    
#     print(ary)
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

# spawn('sample.txt', 80)
# spawn('input.txt', 80)

def spawn2(filename, num_days):
    ary = []
    fish_dict = {}
    for i in range(9):
        fish_dict[i] = 0
    
    with open(filename, 'rt', encoding='utf-8') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            elif char == ',':
                continue
            else:
                fish_dict[int(char)] += 1
    
#     print(fish_dict)
    for day_num in range(num_days):
        zero_fish = fish_dict[0]
        seven_fish = fish_dict[7]
        for fish_idx in range(8):
            if fish_idx == 6:
                continue
            fish_dict[fish_idx] = fish_dict[fish_idx + 1]
        fish_dict[8] = zero_fish
        fish_dict[6] = zero_fish + seven_fish

#         print(f"day {day_num}: {fish_dict}")
    
    ret_sum = 0
    for key in fish_dict:
        ret_sum += fish_dict[key]
    
    print(ret_sum)

spawn2('sample.txt', 80)
spawn2('input.txt', 80)
spawn2('sample.txt', 256)
spawn2('input.txt', 256)