def trajectory(filename):
    tree_grid = []
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            tree_grid.append(line.strip())
    
    height = len(tree_grid)
    width = len(tree_grid[0])
    
    # for row in tree_grid:
        # print(row)
    # print(height)
    # print(width)
    
    curr_row = 0
    curr_col = 0
    count_tree = 0
    while (curr_row < height):
        if tree_grid[curr_row][curr_col % width] == "#":
            count_tree += 1
        curr_row += 1
        curr_col += 3
    
    print(count_tree) # part 1 output

trajectory("sample.txt")
trajectory("input.txt")