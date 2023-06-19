# hill climbing using BFS/dijkstra
# ascii 'a' = 97
# ascii 'z' = 122
from min_heap_node import min_heap
import sys
from collections import deque

class point:
    def __init__(self, row, col, height = None):
        self.row = row
        self.col = col
        self.height = height
    def __str__(self):
        return f"[{self.row}, {self.col}]"
    def __eq__(self, other):
        if other == None:
            return False
        return self.row == other.row and self.col == other.col
    def __hash__(self):
        return hash((self.row, self.col))

def hill_climbing(filename):
    heightmap = []
#     map_start_end = { 'E': ord('z'), 'S': ord('a') }    
    # read input, set start, set end
    with open(filename, 'rt', encoding='utf-8') as file:
        row_num = 0
        for line in file:
            line = line.strip()
            col_num = 0
            for char in line:
                if char == 'S':
                    start = point(row_num, col_num)
                elif char == 'E':
                    end = point(row_num, col_num)
                col_num += 1
            heightmap.append(line)
            row_num +=1
            
    print("debug input heightmap:")
    for row in heightmap:
        print(row)
    print(ord('a'))
    print(ord('z'))
    
    height = len(heightmap)
    width = len(heightmap[0])
#     num_points = height * width
    # create data structures with start point at 0
    dist_dict = { start: 0 }
    prev_dict = { start: None } # start has no prev
    unvisited_heap = min_heap()
#     path_heap.add(start, 0)
    
    for row_num in range(0, height):
        for col_num in range(0, width):
            curr_point = point(row_num, col_num)
            if start != curr_point:
                dist_dict[curr_point] = sys.maxsize
                prev_dict[curr_point] = None
            # add all points to heap with max int except start (start is 0)
            unvisited_heap.add(curr_point, dist_dict[curr_point])   
    print(f"starting dist: {dist_dict}")
    print(f"starting prev: {prev_dict}")
    print(f"starting heap: {unvisited_heap}")
    print(f"start: {start}")
    print(f"end: {end}")
    
    # BFS
    dirs = [(1, 0), # top
        (0, 1), # right
        (-1, 0), # bot
        (0, -1)] # left
    while len(unvisited_heap) > 0:
        curr_point = unvisited_heap.remove()
        curr_height = get_height(heightmap, curr_point.row, curr_point.col)
        print(f"debug - visiting: {curr_point}, height: {curr_height}")
        
        # check four directions
        for dir_tuple in dirs:
            row_vect, col_vect = dir_tuple
            neighbor_row = curr_point.row + row_vect
            neighbor_col = curr_point.col + col_vect
            if neighbor_row < 0 or neighbor_row > height - 1:
                continue
            if neighbor_col < 0 or neighbor_col > width - 1:
                continue
            neighbor_height = get_height(heightmap,
                                         neighbor_row,
                                         neighbor_col)
            print(f" * debug - check neighbor: [{neighbor_row}, {neighbor_col}], height: {neighbor_height}")
            # valid neighbor - down any height and up one height greater
            if neighbor_height <= curr_height + 1:
                print(" * debug - valid neighbor")
                neighbor_point = point(neighbor_row,
                                       neighbor_col)
                test_dist = dist_dict[curr_point] + 1
                if test_dist < dist_dict[neighbor_point]:
                    dist_dict[neighbor_point] = test_dist
                    prev_dict[neighbor_point] = curr_point
                    unvisited_heap.update(neighbor_point, test_dist)
                    print(f"    * debug - update shortest path to {neighbor_point}: {test_dist}")
    
    # output
    path = deque([start])
    curr_parent = prev_dict[end]
    num_moves = 0
    while curr_parent != None:
        path.appendleft(curr_parent)
        curr_parent = prev_dict[curr_parent]
        num_moves += 1
    
    print("debug - output:")
    for curr in path:
        print(curr, end=', ')
    print()
    print(num_moves)
    return
        
def get_height(heightmap, row, col):
    # TODO replace this with map
    char = heightmap[row][col]
    if char == 'S':
        char = 'a'
    elif char == 'E':
        char = 'z'
    return ord(char)

def directions():
    dirs = [(1, 0), # top
            (0, 1), # right
            (-1, 0), # bot
            (0, -1)] # left
    for dir_tuple in dirs:
        row, col = dir_tuple
        print(row, col)

hill_climbing('sample.txt')
# directions()