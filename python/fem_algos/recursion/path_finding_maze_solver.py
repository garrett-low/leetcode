# simple maze solver / path-finding

from typing import Set
from typing import List

class Point: # 0-indexed row, col
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __str__(self):
        return f"[{self.row},{self.col}]"
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __hash__(self):
        return hash(self.row**2 + self.col**2)

def solve(maze, wall, start, end):
    visited: Set[Point] = set()
    path: List[Point] = []
    inner(maze, wall, start, end, visited, path)
    path.reverse()
    
    return path

def inner(maze, wall, curr, end, visited, path):
    if curr in visited:
        return False
    if curr.row >= len(maze) or curr.row < 0:
        return False
    if curr.col >= len(maze[curr.row]) or curr.col < 0:
        return False
    cell_val = maze[curr.row][curr.col]
    if cell_val == wall:
        return False
    
    print(f"debug: visiting {curr}")
    visited.add(curr)
    
    if curr.row == end.row and curr.col == end.col:
        path.append(curr)
        print(f"debug: {curr}")
        return True
    
    if inner(maze, wall, Point(curr.row - 1, curr.col), end, visited, path): # top
        print(f"debug: {curr}")
        path.append(curr)
        return True
    if inner(maze, wall, Point(curr.row, curr.col + 1), end, visited, path): # right
        print(f"debug: {curr}")
        path.append(curr)
        return True
    if inner(maze, wall, Point(curr.row + 1, curr.col), end, visited, path): # bot
        print(f"debug: {curr}")
        path.append(curr)
        return True
    if inner(maze, wall, Point(curr.row, curr.col - 1), end, visited, path): # left
        print(f"debug: {curr}")
        path.append(curr)
        return True
    
    return False

def main():
    maze = ["##### #", "#     #", "# #####"]
    wall = '#'
    start = Point(2, 1) # 0-indexed row, col
    end = Point(0, 5)
    path = solve(maze, wall, start, end)
    print([str(item) for item in path])
    
    maze2 = ["##### #",
             "#     #",
             "# #####",
             "#     #",
             "##### #"]
    start2 = Point(4, 5) # 0-indexed row, col
    end2 = Point(0, 5)
    path2 = solve(maze2, wall, start2, end2)
    print([str(item) for item in path2])
    
if __name__ == "__main__":
    main()