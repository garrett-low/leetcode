def flash(filename, steps = 100):
    octo_map = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            octo_map.append([int(x) for x in line.strip()])
#     print("START")
#     pp(octo_map)
    
    count_flash = 0
    for step_num in range(steps):
        for row_i in range(len(octo_map)):
            for col_i in range(len(octo_map[0])):
                octo_map[row_i][col_i] += 1
        
        for row_i in range(len(octo_map)):
            for col_i in range(len(octo_map[0])):
                count_flash += flash_cascade(octo_map, row_i, col_i)
#         print(f"STEP {step_num}")
#         pp(octo_map)
    print(count_flash)

neighbor_list = [
    (-1, 0), # top
    (-1, 1), # top right
    (0, 1), # right
    (1, 1), # bot right
    (1, 0), # bot
    (1, -1), # bot left
    (0, -1), # left
    (-1, -1) # top left
    ]

def flash_cascade(octo_map, row_i, col_i):
    if octo_map[row_i][col_i] == 0:
        return 0
    elif octo_map[row_i][col_i] > 9:
        octo_map[row_i][col_i] = 0
        recur_flash_count = 0
        for dir_tuple in neighbor_list:
            row_dir, col_dir = dir_tuple
            next_row_i = row_i + row_dir
            next_col_i = col_i + col_dir
            if next_row_i >= len(octo_map) or next_row_i < 0 or next_col_i >= len(octo_map[0]) or next_col_i < 0:
                continue
            if octo_map[next_row_i][next_col_i] == 0:
                continue
            octo_map[next_row_i][next_col_i] += 1
            recur_flash_count += flash_cascade(octo_map, next_row_i, next_col_i)
        recur_flash_count += 1
        return recur_flash_count
    return 0

def pp(octo_map):
    for row_i in range(len(octo_map)):
        for col_i in range(len(octo_map[0])):
            print(octo_map[row_i][col_i], end = '')
        print()
            
flash('sample.txt', 10)
flash('sample.txt')
flash('input.txt')