from collections import defaultdict

DIRS = [
    (-1, -1), # top-left
    (-1, 0), # top
    (-1, 1), # top-right
    (1, -1), # bot-left
    (1, 0), # bot
    (1, 1), # bot-right
    (0, -1), # left
    (0, 1), # right
]

WALL_CHAR = '.'
GEAR_CHAR = '*'

def gear(filename):
    grid = []
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            grid.append(line)
    
    grid_width = len(grid[0])
    grid_height = len(grid)
    
    visited_set = set()
    gear_to_num_start = defaultdict(list)
    num_start_to_num = defaultdict(int)
    
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            start_tuple = (row_idx, col_idx)
            adj_gears = set()
            check_adj_set = set()
            seek_gear_part(grid, row_idx, col_idx, visited_set, start_tuple, gear_to_num_start, num_start_to_num, check_adj_set, False, adj_gears)
    
    # print("GEARS!")
    # for gear in gear_to_num_start:
        # print(gear)
        # print(f"  {gear_to_num_start[gear]}")
            
    # print("GEARS PARTS!")
    # for num_start in num_start_to_num:
        # print(num_start)
        # print(f"  {num_start_to_num[num_start]}")
    
    sum_ratios = 0
    for gear in gear_to_num_start:
        num_starts = gear_to_num_start[gear]
        if len(num_starts) == 2:
            part_one = num_start_to_num[num_starts[0]]
            part_two = num_start_to_num[num_starts[1]]
            sum_ratios += part_one * part_two
    
    print(sum_ratios)
    
def seek_gear_part(grid, i, j, visited_set, start_tuple, gear_to_num_start, num_start_to_num, check_adj_set, has_adj_gear, adj_gears):
    grid_width = len(grid[0])
    grid_height = len(grid)
    if (i, j) in visited_set:
        return False
    if i < 0 or i > (grid_height - 1):
        add_part(grid, start_tuple, j, adj_gears, gear_to_num_start, num_start_to_num)
        return False
    if j < 0 or j > (grid_width - 1):
        add_part(grid, start_tuple, j, adj_gears, gear_to_num_start, num_start_to_num)
        return False
    char = grid[i][j]
    if not char.isdecimal():
        add_part(grid, start_tuple, j, adj_gears, gear_to_num_start, num_start_to_num)
        return False
    
    visited_set.add((i, j))
    
    for dir_tuple in DIRS:
        test_i = i + dir_tuple[0]
        test_j = j + dir_tuple[1]
        has_adj_gear = check_adjacent(grid, test_i, test_j, check_adj_set)
        if has_adj_gear:
            adj_gears.add((test_i, test_j))
    
    is_num = True
    while is_num:
        is_num = seek_gear_part(grid, i, j + 1, visited_set, start_tuple, gear_to_num_start, num_start_to_num, check_adj_set, has_adj_gear, adj_gears)            
    
    return is_num

def check_adjacent(grid, i, j, check_adj_set):
    grid_width = len(grid[0])
    grid_height = len(grid)
    if i < 0 or i >  grid_height - 1:
        return False
    if j < 0 or j > grid_height - 1:
        return False
    if (i, j) in check_adj_set:
        return False
    
    check_adj_set.add((i,j))
    
    char = grid[i][j]
    
    if char == GEAR_CHAR:
        return True
        
    return False

def add_part(grid, start_tuple, j, adj_gears, gear_to_num_start, num_start_to_num):
    if start_tuple[1] == j + 1: # 0 length, nothing to do
        return
    
    for adj_gear in adj_gears:
        gear_to_num_start[adj_gear].append(start_tuple)
    
    if len(adj_gears) > 0:
        part_num = int(grid[start_tuple[0]][start_tuple[1] : j])
        num_start_to_num[start_tuple] = part_num    

gear('sample.txt')
gear('input.txt')