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
        
        # look from top
        print("look from top")
        for col in range(0, grid_width):
            next_max = -1
            next_max_row = 0
            edge_height = int(forest_grid[0][col])
            for row in range(0, grid_width):
                cur_height = int(forest_grid[row][col])
                if cur_height > edge_height and cur_height > next_max:
                    next_max = cur_height
                    next_max_row = row
            
            add_visible_tree(visible_set, 0, col)
            
#             if next_max_row != 0:
            add_visible_tree(visible_set, next_max_row, col)
        
        # look from right
        print("look from right")
        for row in range(0, grid_height):
            next_max = -1
            next_max_col = grid_height - 1
            edge_height = int(forest_grid[row][grid_height - 1])
            for col in range(grid_height - 1, -1, -1):
                cur_height = int(forest_grid[row][col])
                if cur_height > edge_height and cur_height > next_max:
                    next_max = cur_height
                    next_max_col = col
            
            add_visible_tree(visible_set, row, grid_height - 1)
            
#             if next_max_col != grid_height - 1:
            add_visible_tree(visible_set, row, next_max_col)
                
        # look from bot
        print("look from bot")
        for col in range(0, grid_width):
            next_max = -1
            next_max_row = grid_width - 1
            edge_height = int(forest_grid[grid_width - 1][col])
            for row in range(grid_width - 1, -1, -1):
                cur_height = int(forest_grid[row][col])
                if cur_height > edge_height and cur_height > next_max:
                    next_max = cur_height
                    next_max_row = col
            
            add_visible_tree(visible_set, grid_width - 1, col)
            
#             if next_max_row != grid_width - 1:
            add_visible_tree(visible_set, next_max_row, col)
        
        # look from left
        print("look from left")
        for row in range(0, grid_height):
            next_max = -1
            next_max_col = 0
            edge_height = int(forest_grid[row][0])
            for col in range(0, grid_width):
                cur_height = int(forest_grid[row][col])
                if cur_height > edge_height and cur_height > next_max:
                    next_max = cur_height
                    next_max_col = col
            
            add_visible_tree(visible_set, row, 0)
            
#             if next_max_col != 0:
            add_visible_tree(visible_set, row, next_max_col)
    
    print(f"{len(visible_set)}")
    return
    
    
def add_visible_tree(visible_set, row, col):
    visible_tree = Point(row, col)
    print(f"{visible_tree}")
    visible_set.add(visible_tree)

count_visible_trees("input3.txt")
count_visible_trees("input2.txt")
count_visible_trees("input.txt")