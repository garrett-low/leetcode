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

class rock_map:
    def __init__(self, rock_lines, min_row, max_row, min_col, max_col):
        self.rock_lines = rock_lines
        self.min_row = min_row
        self.max_row = max_row
        self.min_col = min_col
        self.max_col = max_col
        #
        self.height = self.max_col - self.min_col + 1
        self.width = self.max_row - self.min_row + 1
        self.grid = [[air for col in range(self.width)] for row in range(self.height)]
    def __str__(self):
        retval = f"{self.min_row}, {self.max_row}, {self.min_col}, {self.max_col}\n"
        for row in self.grid:
            for col in row:
                retval += chr(col)
            retval += "\n"
        return retval

# to make coordinates easier, map is flipped so sand falls up.
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
                p_row = int(point_split[0])
                p_col = int(point_split[1])
                new_point = point(p_row, p_col)
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
    print(min_row)
    print(max_row)
    print(min_col)
    print(max_col)
    
    # make rock_map one unit bigger on all sides (?)
    height = max_col - min_col + 1
    width = max_row - min_row + 1
    rockmap = [[air for col in range(width)] for row in range(height)]
    print_test(rockmap)
    rockmapobj = rock_map(rock_lines, min_row, max_row, min_col, max_col)
    print(rockmapobj)
    
    for rock_line in rock_lines:
        for i in range(len(rock_line) - 1):
            draw_rock(rock_line[i], rock_line[i + 1], rockmap)
    
    print_test(rockmap)

def draw_rock(point1, point2, rockmap):
    print(f"{point1} -> {point2}")
    for row in range(point1.y, point2.y):
        for col in range(point1.x, point2.x):
            rockmap[row][col] = rock

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