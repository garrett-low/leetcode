import copy

DIRS = [(-1, -1),   # top-left
        (-1, 0),    # up
        (-1, 1),    # top-right
        (0, 1),     # right
        (1, 1),     # bot-right
        (1, 0),     # bot
        (1, -1),    # bot-left
        (0, -1)     # left
        ]

MAX_OCCUPIED = 5

def seating_sys(filename):
    seatmap = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            seatmap.append(list(line.strip()))
    
    height = len(seatmap)
    width = len(seatmap[0])
    
    has_changed = True
    # round_i = 0
    while has_changed:
        has_changed = False
        prev_seatmap = copy.deepcopy(seatmap)
        for row_i in range(height):
            for col_i in range(width):
                count_adj_occupied = 0
                
                curr_is_occupied = None
                if seatmap[row_i][col_i] == 'L':
                    curr_is_occupied = False
                elif seatmap[row_i][col_i] == '#':
                    curr_is_occupied = True
                else: # is '.' or floor
                    continue
                
                for dir_tuple in DIRS:
                    row_diff, col_diff = dir_tuple
                    
                    if is_occupied(prev_seatmap, row_i, col_i, row_diff, col_diff):
                        count_adj_occupied += 1
                    
                    # we don't need to continue checking in this case
                    if curr_is_occupied and count_adj_occupied >= MAX_OCCUPIED:
                        break
                
                if curr_is_occupied and count_adj_occupied >= MAX_OCCUPIED:
                    seatmap[row_i][col_i] = 'L'
                    has_changed = True
                    continue
                
                if not curr_is_occupied and count_adj_occupied == 0:
                    seatmap[row_i][col_i] = '#'
                    has_changed = True
                    continue
        
        # round_i += 1
        # print(f"~\t{round_i}\t~")
        # printdebug(seatmap)
    
    # P1 answer
    count_occupied = 0
    for row in range(height):
        for col in range(width):
            if seatmap[row][col] == '#':
                count_occupied += 1
    
    print(f"P1:\t{count_occupied}")

def is_occupied(seatmap, row, col, row_diff, col_diff):
    test_row = row + row_diff
    test_col = col + col_diff
    
    # off the map
    if test_row < 0 or test_row >= len(seatmap) or test_col < 0 or test_col >= len(seatmap[0]):
        return False
    
    curr = seatmap[test_row][test_col]
    if curr == 'L':
        return False
    if curr == '#':
        return True
    if curr == '.':
        return is_occupied(seatmap, test_row, test_col, row_diff, col_diff)
    
    return False

def printdebug(seatmap):
    for row in range(len(seatmap)):
        for col in range(len(seatmap[0])):
            print(seatmap[row][col], end='')
        print()

seating_sys('sample.txt')
# seating_sys('input.txt')

# P1 answer is 2476
# P2 sample: 26
# P2: 2257