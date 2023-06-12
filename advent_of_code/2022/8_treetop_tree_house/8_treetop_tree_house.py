# 8_treetop_tree_house
# global variables are bad blah blah
visible_tree_set = set()
found_visible_row = set()
found_visible_col = set()
grid_height = 0
grid_width = 0

class Point:
    def __init__(self, row, col, height = 0):
        self.row = row
        self.col = col
        self.height = height
    def __str__(self):
        return f"[{self.row}, {self.col}], height: {self.height}"
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __hash__(self):
        # https://stackoverflow.com/a/682617/21593883
        return hash(((self.row + self.col) * (self.row + self.col + 1)/2) + self.col)
            #(self.row**2 + self.col**2)
    
def count_visible_trees_2():
    pass

def count_visible_trees():
    forest_grid = []
    global grid_height
    global grid_width
    global found_visible_row
    global found_visible_col
    global visible_tree_set
    grid_height = 0
    grid_width = 0
    found_visible_row = set()
    found_visible_col = set()
    visible_tree_set = set()
    visible_tree_count = 0
    
    with open('input.txt', 'rt', encoding='utf-8') as file:
        for line in file:
            forest_grid.append(line.strip())
            grid_height += 1
    
    grid_width = len(forest_grid[0])
    print(f"{grid_height}, {grid_width}")
    
    # search
    for row in range(0, grid_height):
        for col in range(0, grid_width):
#             if col in found_visible_col:
#                 continue # skip this col
            
            tree = Point(row, col, forest_grid[row][col])
            
            if is_visible(row, col, forest_grid):
#                 print(tree)
                visible_tree_set.add(tree)
                found_visible_row.add(row)
                found_visible_col.add(col)
                visible_tree_count += 1
                
#                 break # stop searching this row
    
#     is_visible(2, 36, forest_grid)
    
    print(f"{len(visible_tree_set) + (2 * grid_height) + (2 * grid_width) - 4}")
#     print(f"{visible_tree_count}")

def is_visible(row, col, forest_grid):
    height = forest_grid[row][col]
#     print(f"{row}, {col}, {height}")
    if not recurse_up(row - 1, col, height, forest_grid):
        return False
    if not recurse_right(row, col + 1, height, forest_grid):
        return False
    if not recurse_down(row + 1, col, height, forest_grid):
        return False
    if not recurse_left(row, col - 1, height, forest_grid):
        return False
    return True
    
def recurse_up(row, col, my_height, forest_grid):
    if row < 0:
        return True    
    cur_height = forest_grid[row][col]
#     print(f"up: {row}, {col}, {my_height}, {cur_height}")
    if cur_height > my_height:
        return False
    if recurse_up(row - 1, col, my_height, forest_grid):
        return True
    
    return False

def recurse_right(row, col, my_height, forest_grid):
    if col >= grid_width:
        return True
    cur_height = forest_grid[row][col]
#     print(f"right: {row}, {col}, {my_height}, {cur_height}")
    if cur_height > my_height:
        return False
    if recurse_right(row, col + 1, my_height, forest_grid):
        return True
    
    return False
def recurse_down(row, col, my_height, forest_grid):
    if row >= grid_height:
        return True
    cur_height = forest_grid[row][col]
#     print(f"down: {row}, {col}, {my_height}, {cur_height}")
    if cur_height > my_height:
        return False
    if recurse_down(row + 1, col, my_height, forest_grid):
        return True
    
    return False
def recurse_left(row, col, my_height, forest_grid):
    if col < 0:
        return True
    cur_height = forest_grid[row][col]
#     print(f"left: {row}, {col}, {my_height}, {cur_height}")
    if cur_height > my_height:
        return False
    if recurse_left(row, col - 1, my_height, forest_grid):
        return True
    
    return False

# def recurse(row, col, prev_height):
#     # edges automatically visible
#     if row < 1 or col < 1:
#         return False
#     if row >= grid_height or col <= grid_width:
#         return False
#     
#     cur_height = forest_grid[row][col]
#     tree = Point(row, col, cur_height)
#     if tree in visited_set:
#         return False
#     
#     visited_set.append(tree)
#     
#     if cur_height >= prev_height:
#         return True
#     
#     if recurse(row - 1, col, cur_height):
#         return True
#     
#     return False
#     
#     for row in forest_grid:
#         print(row)
        
# count_visible_trees()