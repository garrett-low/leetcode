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

print("PART ONE")
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
    
    # I misread the problem and started adding the heights of positions in the basin.
    # Ignore all that
    basin_size_list = []
    for point_tuple in lowpoint:
        row_idx, col_idx = point_tuple
        visited = set()
        traverse(heightmap, row_idx, col_idx, rows_num, cols_num, visited)
        basin_size_list.append(len(visited))
    qs(basin_size_list)
    
    basin_top_product = 1
    for i in range(3):
        basin_top_product *= basin_size_list[i]
    print(basin_top_product)
    return

def traverse(heightmap, row_idx, col_idx, rows_num, cols_num, visited):
    if (row_idx, col_idx) in visited:
        return 0
    if row_idx >= rows_num or row_idx < 0 or col_idx >= cols_num or col_idx < 0:
        return 0
    curr = heightmap[row_idx][col_idx]
    if curr >= 9:
        return 0
       
    visited.add((row_idx, col_idx))
    basin_sum = heightmap[row_idx][col_idx]
    
    for dir_tuple in directions:
        rowdiff, coldiff = dir_tuple
        row_test = row_idx - rowdiff
        col_test = col_idx - coldiff
        basin_sum += traverse(heightmap, row_test, col_test, rows_num, cols_num, visited)
    
    return basin_sum

def qs(arr):
    qs_inner(arr, 0, len(arr) - 1)

def qs_inner(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    p = pivot(arr, lo, hi)
    qs_inner(arr, p + 1, hi)
    qs_inner(arr, lo, p - 1)
    
def pivot(arr, lo, hi):
    p = arr[hi]
    p_idx = lo - 1
    
    for i in range(lo, hi):
        if arr[i] > p:
            p_idx += 1
            temp = arr[i]
            arr[i] = arr[p_idx]
            arr[p_idx] = temp
    
    p_idx += 1
    arr[hi] = arr[p_idx]
    arr[p_idx] = p
    return p_idx

print("PART TWO")
smoke_two('sample.txt')
smoke_two('input.txt')