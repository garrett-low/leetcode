import sys

rock = 9608
air = 9617
sand = 9679

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"[{self.x}, {self.y}]"

# make rock_map one unit bigger on left and right
class rock_map:
    def __init__(self, rock_lines, min_row, max_row, min_col, max_col):
        self.rock_lines = rock_lines
        self.min_row = min_row
        self.max_row = max_row
        self.min_col = min_col
        self.max_col = max_col
        # empty grid
        self.width = self.max_col - self.min_col + 2
        self.height = self.max_row + 5
        self.grid = [[air for col in range(self.width)] for row in range(self.max_row + 5)]
        #
        for rock_line in rock_lines:
            for i in range(len(rock_line) - 1):
                self.draw_rock(rock_line[i], rock_line[i + 1])      
        
    def __str__(self):
        retval = f"{self.min_row}, {self.max_row}, {self.min_col}, {self.max_col}\n"
        retval += " "
        for i in range(self.width):
            retval += f"{i % 9}"
        retval += "\n"
        i = 0
        for row in self.grid:
            retval += f"{i % 9}"
            for col in row:
                retval += chr(col)
            retval += "\n"
            i += 1
        return retval
    
    def draw_rock(self, point1, point2):
        if point1.x == point2.x:
            if point1.y < point2.y:
                row_start = point1.y
                row_end = point2.y
            else:
                row_start = point2.y
                row_end = point2.y
            # inclusive of end point
            for row in range(row_start, row_end + 1):
                self.grid[row][self.getx(point1.x)] = rock
        else:
            if point1.x < point2.x:
                col_start = point1.x
                col_end = point2.x
            else:
                col_start = point2.x
                col_end = point1.x
            # inclusive of end point
            for col in range(col_start, col_end + 1):
                self.grid[point1.y][self.getx(col)] = rock
    
    def getx(self, x):
        return x - self.min_col + 1

def falling_sand(filename):    
    min_row = sys.maxsize
    min_col = sys.maxsize
    max_row = 0
    max_col = 0
    rock_lines = []
    with open(filename, 'rt', encoding='utf-8') as file:
        rock_line_idx = 0
        for line in file:
            line_split = line.split(' -> ')
            rock_lines.append([])
            # Find min and max row so I don't have to draw an arbitrarily large grid. Yes this means two passes
            for point_str in line_split:
                point_split = point_str.split(',')
                p_col = int(point_split[0])
                p_row = int(point_split[1])
                new_point = point(p_col, p_row)
                rock_lines[rock_line_idx].append(new_point)
                if p_row < min_row:
                    min_row = p_row
                elif p_row > max_row:
                    max_row = p_row
                if p_col < min_col:
                    min_col = p_col
                elif p_col > max_col:
                    max_col = p_col
            rock_line_idx += 1  
#     print(min_row)
#     print(max_row)
#     print(min_col)
#     print(max_col)
    
    rockmapobj = rock_map(rock_lines, min_row, max_row, min_col, max_col)
    print(rockmapobj)

def print_test(arr):
#     arr = [[air for col in range(10)] for row in range(10)]
#     print(chr(rock))
#     print(chr(air))
#     print(chr(sand))
    for row in arr:
        for col in row:
            print(chr(col), end='')
        print()

falling_sand('sample.txt')