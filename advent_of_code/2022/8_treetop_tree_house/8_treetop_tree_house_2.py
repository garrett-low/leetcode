# treetop tree house

def count_visible_trees():
    forest_grid = []
    grid_height = 0
    grid_width = 0
    
    with open('input.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        forest_grid.append(line.strip())
        grid_height += 1
        
    grid_width = len(forest_grid[0])