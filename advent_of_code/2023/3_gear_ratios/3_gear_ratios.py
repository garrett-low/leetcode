DIRS = [
    (-1, -1) # top-left
    (-1, 0), # top
    (-1, 1), # top-right
    (1, -1), # bot-left
    (1, 0), # bot
    (1, 1), # bot-right
    (0, -1), # left
    (0, 1), # right
]

WALL_CHAR = '.'

GRID_WIDTH = 0
GRID_HEIGHT = 0

VISITED_SET = set()
PART_NUMS = []

def gear(filename):
    grid = []
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            grid.append(line)
    
    print(grid)
    
    GRID_WIDTH = len(grid[0])
    GRID_HEIGHT = len(grid)
    
    # seen_coord_set = set()
    # seen_val_set = set()
    
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            if char.isalnum() or char == WALL_CHAR:
                continue
            
            adj_nums = find_adj_nums(grid, (row_idx, col_idx))
            

def find_adj_nums(grid, coord_tuple):
    row_idx, col_idx = coord_tuple
    
    for dir_tuple in DIRS:
        test_coord_tuple = (row_idx + dir_tuple[0], col_idx + dir_tuple[1])
        is_test_coord_numeric = check_adjacent(grid, test_coord_tuple)
        
        if is_test_coord_numeric:
            seek_num(grid, test_coord_tuple[0], test_coord_tuple[1])
        
def check_adjacent(grid, test_coord_tuple):
    i, j = test_coord_tuple
    
    if i < 0 or i > GRID_HEIGHT - 1:
        return False
    
    if j < 0 or j > GRID_WIDTH - 1:
        return False
    
    test_char = grid[i][j]
    
    if test_char.isdecimal():
        return True

def seek_num(grid, i, j):
    

gear('sample.txt')