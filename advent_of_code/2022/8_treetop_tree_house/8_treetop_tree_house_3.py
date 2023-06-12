# treetop tree house

class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __str__(self):
        return f"[{self.row}, {self.col}]"
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __hash__(self):
         # https://stackoverflow.com/a/682617/21593883
        return hash(((self.row + self.col) * (self.row + self.col + 1)/2) + self.col)

def count_visible_trees(filename):
    forest_grid = []
    grid_height = 0
    grid_width = 0
    visible_set = set()
    
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            forest_grid.append(line.strip())
            grid_height += 1
            
        grid_width = len(forest_grid[0])
        
        # look right
        for row in range(0, grid_height):
            cur_max = -1
            for col in range(0, grid_width):
                cur_height = int(forest_grid[row][col])
                if cur_height > cur_max:
                    add_visible_tree(visible_set, row, col)
                    cur_max = cur_height
        
        # look down
        for col in range(0, grid_height):
            cur_max = -1
            for row in range(0, grid_width):
                cur_height = int(forest_grid[row][col])
                if cur_height > cur_max:
                    add_visible_tree(visible_set, row, col)
                    cur_max = cur_height
        
        # look left
        for row in range(0, grid_height):
            cur_max = -1
            for col in range(grid_width - 1, -1, -1):
                cur_height = int(forest_grid[row][col])
                if cur_height > cur_max:
                    add_visible_tree(visible_set, row, col)
                    cur_max = cur_height
        
        # look up
        for col in range(0, grid_height):
            cur_max = -1
            for row in range(grid_width - 1, -1, -1):
                cur_height = int(forest_grid[row][col])
                if cur_height > cur_max:
                    add_visible_tree(visible_set, row, col)
                    cur_max = cur_height
    
    print(f"{len(visible_set)}")
    return

def add_visible_tree(visible_set, row, col):
    visible_tree = Point(row, col)
#     print(f"{visible_tree}")
    visible_set.add(visible_tree)
    
count_visible_trees("input3.txt")
count_visible_trees("input2.txt")
count_visible_trees("input.txt")