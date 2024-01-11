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
            [(-1, 0), # up
             (0, 1)] # right
            }
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

def dfs(grid, curr, visited_set, path):
    # outside bounds
    if curr[0] < 0 or curr[0] >= len(grid):
        return False
    if curr[1] < 0 or curr[1] >= len(grid[0]):
        return False

    val = grid[curr[0]][curr[1]]
    if val == START: # seeking cycle; START is end
        return True
    if val == GROUND:
        return False

    if val not in PIPE_DIR:
        print("This is impossible")
        return False

    dirs = PIPE_DIR[val]

    for movetuple in dirs:
        dest = (curr[0] + movetuple[0], curr[1] + movetuple[1])
        if dfs(grid, dest, visited_set, path):
            return True


pipes('sample1.txt')
