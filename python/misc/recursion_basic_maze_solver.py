# simple maze solver / path-finding
DIRS_TUPLE = [(-1, 0), # top
              (0, 1), # right
              (1, 0), # bot
              (0, -1) # left
              ]

class Point: # 0-indexed row, col
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __str__(self):
        return f"[{self.row},{self.col}]"
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __hash__(self):
        # https://stackoverflow.com/a/682617/21593883
        return hash((self.row, self.col))

def solve(maze, wall, start, end):
    visited = set()
    path = []
    inner(maze, wall, start, end, visited, path)
    path.reverse()
    
    return path

def inner(maze, wall, curr, end, visited, path):
    if curr in visited:
        return False
    if curr.row >= len(maze) or curr.row < 0:
        return False
    if curr.col >= len(maze[curr.row]) or curr.col < 0:
        return False
    cell_val = maze[curr.row][curr.col]
    if cell_val == wall:
        return False
    
    # print(f"debug: visiting {curr}")
    visited.add(curr)
    
    if curr.row == end.row and curr.col == end.col:
        path.append(curr)
        # print(f"debug: {curr}")
        return True
    
    for dir_tuple in DIRS_TUPLE:
        row_diff, col_diff = dir_tuple
        test_row = curr.row + row_diff
        test_col = curr.col + col_diff
        if inner(maze, wall, Point(test_row, test_col), end, visited, path):
            path.append(curr)
            return True
    
    return False

def main():
    maze = ["##### #",
            "#     #",
            "# #####"]
    wall = '#'
    start = Point(2, 1) # 0-indexed row, col
    end = Point(0, 5)
    path = solve(maze, wall, start, end)
    print([str(item) for item in path])
    
    maze2 = ["##### #",
             "#     #",
             "# #####",
             "#     #",
             "##### #"]
    start2 = Point(4, 5) # 0-indexed row, col
    end2 = Point(0, 5)
    path2 = solve(maze2, wall, start2, end2)
    print([str(item) for item in path2])
    
    maze_out_of_bounds = ["# ### #",
                          "#     #",
                          "  #####",
                          "#     #",
                          "##### #"]
    start3 = Point(4, 5) # 0-indexed row, col
    end3 = Point(0, 5)
    path3 = solve(maze_out_of_bounds, wall, start3, end3)
    print([str(item) for item in path3])
    
if __name__ == "__main__":
    main()