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

# VISITED_SET = set()

def gear(filename):
    grid = []
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            grid.append(line)
    
    grid_width = len(grid[0])
    grid_height = len(grid)
    # print(grid)
    # print(f"{grid_width} {grid_height}")
    
    visited_set = set()
    valid_part_nums = []
    
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            start_tuple = (row_idx, col_idx)
            is_num, has_adj_symbol, end_tuple = seek_num(grid, row_idx, col_idx, visited_set, False)
            # print(start_tuple, has_adj_symbol, end_tuple)
            if has_adj_symbol:
                val = int(grid[row_idx][col_idx : end_tuple[1]])
                valid_part_nums.append(val)
    
    # print(valid_part_nums)
    sum = 0
    for val in valid_part_nums:
        sum += val
        print(val)
    
    print(sum)

def seek_num(grid, i, j, visited_set, has_adj_symbol = False):
    # print(f"{char} [{i}][{j}]")
    grid_width = len(grid[0])
    grid_height = len(grid)
    # print(grid_width, grid_height)
    if (i, j) in visited_set:
        # print("2")
        return False, has_adj_symbol, (i, j)
    if i < 0 or i > (grid_height - 1):
        # print("3")
        return False, has_adj_symbol, (i, j)
    if j < 0 or j > (grid_width - 1):
        # print("4")
        return False, has_adj_symbol, (i, j)
    char = grid[i][j]
    if not char.isdecimal():
        # print("1")
        return False, has_adj_symbol, (i, j)
    
    visited_set.add((i, j))
    
    if not has_adj_symbol:
        for dir_tuple in DIRS:
            test_i = i + dir_tuple[0]
            test_j = j + dir_tuple[1]
            # print(test_i, test_j)
            has_adj_symbol = check_adjacent(grid, test_i, test_j)
            if has_adj_symbol:
                break
    
    is_num = True
    while is_num:
        is_num, has_adj_symbol, end_tuple = seek_num(grid, i, j + 1, visited_set, has_adj_symbol)
        
    return is_num, has_adj_symbol, end_tuple

def check_adjacent(grid, i, j):
    grid_width = len(grid[0])
    grid_height = len(grid)
    if i < 0 or i >  grid_height - 1:
        return False
    if j < 0 or j > grid_height - 1:
        return False
    
    char = grid[i][j]
    
    if not char.isalnum() and char != WALL_CHAR:
        # print(f"{i}, {j}")
        return True
        
    return False

gear('sample.txt')
gear('input.txt')

# 527987: first attempt, too low
# 528819: removing random global variables that are poor style,
#   but also apparently have a functional impact - 
#   no other changes