# part two
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

class Grid:
    def __init__(self, array, grid_height, grid_width):
        self.array = array
        self.grid_height = grid_height
        self.grid_width = grid_width

def find_scenic_tree(filename):
    forest_array = []
    grid_height = 0
    grid_width = 0
    
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            forest_array.append(line.strip())
            grid_height += 1
            
        grid_width = len(forest_array[0])
        grid = Grid(forest_array, grid_height, grid_width)        
        
        max_score = 0
        for row in range(0, grid_height):
            for col in range(0, grid_width):                
                score = calc_score(row, col, grid)
                if score > max_score:
                    max_score = score
    
#     print(score(3, 2, grid))
    
    print(max_score)

def calc_score(row, col, grid):
    my_height = grid.array[row][col]
    count_up = look_up(row, col, my_height, grid)
    count_right = look_right(row, col, my_height, grid)
    count_down = look_down(row, col, my_height, grid)
    count_left = look_left(row, col, my_height, grid)
#     print(f"top: {count_up}, right: {count_right}, bot: {count_down}, left: {count_left}")
    return count_up * count_right * count_down * count_left

def look_up(row, col, my_height, grid):
    count = 0
    for r in range(row - 1, -1, -1):
        cur_height = grid.array[r][col]
        count += 1
        if cur_height >= my_height:
            break
    
    return count

def look_right(row, col, my_height, grid):
    count = 0
    for c in range(col + 1, grid.grid_width):
        cur_height = grid.array[row][c]
        count += 1
        if cur_height >= my_height:
            break
    
    return count

def look_down(row, col, my_height, grid):
    count = 0
    for r in range(row + 1, grid.grid_height):
        cur_height = grid.array[r][col]
        count += 1
        if cur_height >= my_height:
            break
    
    return count

def look_left(row, col, my_height, grid):
    count = 0
    for c in range(col - 1, -1, -1):
        cur_height = grid.array[row][c]
        count += 1
        if cur_height >= my_height:
            break
    
    return count
                
find_scenic_tree("input2.txt")
find_scenic_tree("input.txt")