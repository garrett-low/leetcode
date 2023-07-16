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