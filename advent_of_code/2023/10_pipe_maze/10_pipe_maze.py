from collections import deque

PIPE_DIR = { '-' :
            [(0, 1), # right
             (0, -1)], # left
            '|' :
            [(-1, 0), # up
             (1, 0)], # down
            '7' :
            [(1, 0), # down
             (0, -1)], # left
            'F' :
            [(1, 0), # down
             (0, 1)], # right
            'L' :
            [(-1, 0), # up
             (0, 1)], # right
            'J' :
            [(-1, 0), # up
             (0, -1)], # left
            }
START_DIRS = [
        [-1, 0], # top
        [0, 1], # right
        [1, 0], # bot
        [0, -1]] # left
START = 'S'
GROUND = '.'
def pipes(filename):
    grid = []
    with open(filename, 'rt') as file:
        for line in file:
            grid.append(line.strip())
    print(grid)

    # find starting coord
    start = None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == START:
                start = (i, j)
                break
    print(start)
    
    path = []
    visited_set = set()
    length = 0
    dfs(grid, start, visited_set, path, length)
    print(path)
    print(length)

def dfs(grid, curr, visited_set, path, length):
    if curr in visited_set:
        return False
    # outside bounds
    if curr[0] < 0 or curr[0] >= len(grid):
        return False
    if curr[1] < 0 or curr[1] >= len(grid[0]):
        return False

    val = grid[curr[0]][curr[1]]
    if val == GROUND:
        return False

    if val not in PIPE_DIR and length != 0:
        print("This is impossible")
        return False

    path.append(curr)
    visited_set.add(curr)
    print(f"{curr[0]}, {curr[1]}, {val}")
    if val == START and length != 0: # seeking cycle; START is end
        print(path)
        print(length)
        return True
    # if val == START and length == 0:
    #     visited_set.remove(curr)
    # length += 1

    dirs = None
    if val == START and length == 0:
        dirs = START_DIRS
    else:
        dirs = PIPE_DIR[val]

    for move_tuple in dirs:
        dest = (curr[0] + move_tuple[0], curr[1] + move_tuple[1])
        if dfs(grid, dest, visited_set, path, length):
            length += 1
            return True
    visited_set.remove(curr)
    path.pop()
    length += 1
    return False

pipes('sample1.txt')
