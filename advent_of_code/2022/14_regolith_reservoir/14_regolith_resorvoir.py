import sys

rock = 9608
air = 9617
sand = 9679

class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

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
            # Find min and max row so I don't have to draw an arbitrarily large grid
            # Yes this means two passes
            for point_str in line_split:
                point_split = point_str.split(',')
                p_row = int(point_split[0])
                p_col = int(point_split[1])
                point = Point(p_row, p_col)
                rock_lines[rock_line_idx].append(point)
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

def draw_rock(point1, point2):
    pass

def print_test(arr):
#     arr = [[air for col in range(10)] for row in range(10)]
    for row in arr:
        for col in row:
            print(chr(col), end='')
        print()

print(chr(rock))
print(chr(air))
print(chr(sand))

falling_sand('sample.txt')