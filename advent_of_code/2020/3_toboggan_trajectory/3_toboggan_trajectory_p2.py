TEST_SLOPES = [(1, 1),
                (1, 3),
                (1, 5),
                (1, 7),
                (2, 1)]

def trajectory(filename):
    tree_grid = []
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            tree_grid.append(line.strip())
    
    product_count_tree = 1
    for slope_tuple in TEST_SLOPES:
        product_count_tree *= count_trees(tree_grid, slope_tuple)
    
    print(product_count_tree) # part 2 output

def count_trees(tree_grid, slope_tuple):
    height = len(tree_grid)
    width = len(tree_grid[0])
    
    move_row, move_col = slope_tuple
    curr_row = 0
    curr_col = 0
    count_tree = 0
    while (curr_row < height):
        if tree_grid[curr_row][curr_col % width] == "#":
            count_tree += 1
        curr_row += move_row
        curr_col += move_col
    
    return count_tree

trajectory("sample.txt")
trajectory("input.txt")