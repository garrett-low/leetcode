directions = [(0, 1),
              (1, 0),
              (0, -1),
              (-1, 0)]

def smoke(filename):
    heightmap = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            heightmap.append([int(x) for x in line.strip()])
    
#     print(heightmap)
    lowpoint = []
    for row_idx in range(len(heightmap)):
        for col_idx in range(len(heightmap[row_idx])):
            curr = heightmap[row_idx][col_idx]
            is_not_lowpoint = False
            for dir_tuple in directions:
                rowdiff, coldiff = dir_tuple
                row_test = row_idx - rowdiff
                col_test = col_idx - coldiff
                if row_test >= len(heightmap) or row_test < 0 or col_test >= len(heightmap[row_idx]) or col_test < 0:
                    continue
                if curr >= heightmap[row_idx - rowdiff][col_idx - coldiff]:
                    is_not_lowpoint = True
                    break
            if not is_not_lowpoint:
                lowpoint.append(curr)
    
#     print(lowpoint)
    retval = 0
    for point in lowpoint:
        retval += point + 1
    print(retval)
    
    return

smoke('sample.txt')
smoke('input.txt')

def smoke_two(filename):
    heightmap = []

    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            heightmap.append([int(x) for x in line.strip()])
    
    lowpoint = []
    rows_num = len(heightmap)
    cols_num = len(heightmap[0])
    for row_idx in range(rows_num):
        for col_idx in range(cols_num):
            curr = heightmap[row_idx][col_idx]
            is_not_lowpoint = False
            for dir_tuple in directions:
                rowdiff, coldiff = dir_tuple
                row_test = row_idx - rowdiff
                col_test = col_idx - coldiff
                if row_test >= len(heightmap) or row_test < 0 or col_test >= len(heightmap[row_idx]) or col_test < 0:
                    continue
                if curr >= heightmap[row_idx - rowdiff][col_idx - coldiff]:
                    is_not_lowpoint = True
                    break
            if not is_not_lowpoint:
                lowpoint.append((row_idx, col_idx))
    
    basin_sum_list = []
    for point_tuple in lowpoint:
        row_idx, col_idx = point_tuple
        visited = set()
        basin_sum = 0
        traverse(heightmap, row_idx, col_idx, rows_num, cols_num, visited, basin_sum)
        print(visited)
        print(basin_sum)

def traverse(heightmap, row_idx, col_idx, rows_num, cols_num, visited, basin_sum):
    if (row_idx, col_idx) in visited:
        return False
    if row_idx >= rows_num or row_idx < 0 or col_idx >= cols_num or col_idx < 0:
        return False
    curr = heightmap[row_idx][col_idx]
    if curr >= 9:
        return False
    
    visited.add((row_idx, col_idx))
    
    for dir_tuple in directions:
        rowdiff, coldiff = dir_tuple
        row_test = row_idx - rowdiff
        col_test = col_idx - coldiff
        if traverse(heightmap, row_test, col_test, rows_num, cols_num, visited, basin_sum):
            basin_sum += heightmap[row_test][col_test]
            return True
    
    return False

smoke_two('sample.txt')