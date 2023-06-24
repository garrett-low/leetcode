import sys
# import os

rock = 9608
air = 9617
sand = 9679
sand_x = 500

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
        self.width = self.max_col - self.min_col + 3 # inclusive of endpoint
        self.height = self.max_row + 5
        self.grid = [[air for col in range(self.width)] for row in range(self.height)]
        #
        for rock_line in rock_lines:
            for i in range(len(rock_line) - 1):
                self.draw_rock(rock_line[i], rock_line[i + 1])
        #
#         self.origin_x = sand_x - self.min_row + 1 # padding left
#         self.origin_y = 0
        self.move_dir = [(0, 1),  # down
                         (-1, 1), # down and left
                         (1, 1)]  # down and right
        
    def __str__(self):
        retval = f"{self.min_row}, {self.max_row}, {self.min_col}, {self.max_col}\n"
        
        retval += " "
        for i in range(self.width):
            retval += f"{i % 10}"
        retval += "\n"
        i = 0
        
        for row in self.grid:
            retval += f"{i % 10}"
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
    
    def sim_sand(self):
        i = 0
        sand_origin_x = self.getx(sand_x)
        sand_origin_y = 0
        
#         new_sand = point(sand_origin_x, sand_origin_y)
#         self.fall(new_sand)
        
        # Sand falls one at a time
        done = False
        while done != None:
            new_sand = point(sand_origin_x, sand_origin_y)
            done = self.fall(new_sand)
            i += 1
        return i - 1 # minus the one that fell into the void
    
    def fall(self,curr):
#         origin = point(curr.x, curr.y)
#         prev = None
        done = False
        
        while not done:
            prev = point(curr.x, curr.y)
            for dir_tuple in self.move_dir: # checked in list's order
                x, y = dir_tuple
#                 print(f"debug: check [{x}, {y}]")
                
                # Into the void
                if curr.y + y >= self.height:
                    print(f"debug: void: {curr.x}, {curr.y} + {y}")
                    return None
                if curr.x + x < 0 or curr.x + x >= self.width:
                    print(f"debug: void: {curr.x} + {x}, {curr.y}")
                    return None
                
                if self.grid[curr.y + y][curr.x + x] == air:
                    curr.x += x
                    curr.y += y
#                     print(f"debug: [{curr.x}, {curr.y}]")
                    break # out of the for loop
            done = self.is_at_rest(curr, prev)
        
        # sand falls one at a time, move it
        self.grid[curr.y][curr.x] = sand
#         print(f"debug: {chr(self.grid[curr.y][curr.x])} at [{curr.x}, {curr.y}]")
        
        return done
                
        
    def is_at_rest(self, curr, prev):
        # rest
        if prev.x == curr.x and prev.y == curr.y:
            return True
        # still not at rest
        return False

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
    
    rockmapobj = rock_map(rock_lines, min_row, max_row, min_col, max_col)
    print(rockmapobj)
    num_sand = rockmapobj.sim_sand()
    print(rockmapobj)
    print(num_sand)

def print_test(arr):
#     arr = [[air for col in range(10)] for row in range(10)]
#     print(chr(rock))
#     print(chr(air))
#     print(chr(sand))
    for row in arr:
        for col in row:
            print(chr(col), end='')
        print()

# falling_sand('sample.txt')
falling_sand('input.txt')