# simple maze solver / path-finding

from typing import Set
from typing import List

class Point: # 0-indexed row, col
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __str__(self):
        return f"[{self.row},{self.col}]"

def solve(maze, wall, start, end):
    visited: Set[Point] = set()
    path: List[Point] = []
    inner(maze, wall, start, end, visited, path)
    path.reverse()
    
    return path

def inner(maze, wall, curr, end, visited, path):
    if curr in visited:
        return False
    visited.add(curr)
    
    if curr.row >= len(maze):
        return False
    if curr.col >= len(maze[curr.row]):
        return False
    
    cell_val = maze[curr.row][curr.col]
    if cell_val == '#':
        return False
    if curr.row == end.row and curr.col == end.col:
        path.append(curr)
        return True
    
    if inner(maze, wall, Point(curr.row - 1, curr.col), end, visited, path): # top
        path.append(curr)
        return True
    if inner(maze, wall, Point(curr.row, curr.col + 1), end, visited, path): # right
        path.append(curr)
        return True
    if inner(maze, wall, Point(curr.row + 1, curr.col), end, visited, path): # bot
        path.append(curr)
        return True
    if inner(maze, wall, Point(curr.row, curr.col - 1), end, visited, path): # left
        path.append(curr)
        return True

def main():
    maze = ["##### #", "#     #", "# #####"]
    wall = '#'
    start = Point(2, 1) # 0-indexed row, col
    end = Point(1, 5)
    blahblah = [start, end]
    print([str(item) for item in blahblah])
    path = solve(maze, wall, start, end)
    print([str(item) for item in path])
    
if __name__ == "__main__":
    main()