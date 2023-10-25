DIRS = { 'N' : (-1, 0), # north
         'W' : (0, -1), # west
         'S' : (1, 0), # south
         'E' : (0, 1)} # east

DIR_ORDER = ['N', 'E', 'S', 'W']

START = (0, 0)
START_DIR_IDX = 1

def rain_risk(filename):
    curr_pos = START
    curr_dir_idx = START_DIR_IDX
    curr_dir = DIR_ORDER[curr_dir_idx]
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            action = line[0]
            value = int(line[1:])
            
            # print(f'{action} {value}')
            
            if action == 'L' or action == 'R':
                cardinal_steps = value // 90
                
                if action == 'R':
                    curr_dir_idx = (curr_dir_idx + cardinal_steps) % 4
                else:
                    curr_dir_idx = (curr_dir_idx - cardinal_steps) % 4 
                # print(f'  Rotated to {DIR_ORDER[curr_dir_idx]}')
            else:
                if action == 'F':
                    curr_dir = DIR_ORDER[curr_dir_idx]
                else:
                    curr_dir = action
            
                dir_multiplier = DIRS[curr_dir]
                # print(f'  Facing {curr_dir}, {dir_multiplier}, Moving {value}')
                curr_pos = (curr_pos[0] + dir_multiplier[0] * value, curr_pos[1] + dir_multiplier[1] * value)
                
            # print(f'  {curr_pos}')
            # print(f'  {DIR_ORDER[curr_dir_idx]}')
    print(f'P1: {abs(curr_pos[0]) + abs(curr_pos[1])}')

rain_risk('sample.txt')
rain_risk('input.txt')