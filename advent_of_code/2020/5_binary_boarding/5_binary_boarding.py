ROW_MAX = 127
COL_MAX = 7

def boarding(filename):
    max_seat_id = 0
    
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            line = line.strip()
            row_search = line[:7]
            col_search = line[7:]
            
            row_id = partition(row_search, 0, ROW_MAX)
            col_id = partition(col_search, 0, COL_MAX)
            seat_id = row_id * 8 + col_id
            # print(row_id, col_id, seat_id)
            if seat_id > max_seat_id:
                max_seat_id = seat_id
    
    print(max_seat_id)

def partition(bsp_string, lo, hi):
    for ch in bsp_string:
        mid = ((hi - lo) // 2) + lo
        if ch == 'F' or ch == 'L':
            hi = mid
        else:
            lo = mid + 1
    
    return lo

# print(partition('FBFBBFF', 0, 127))
boarding('sample1.txt')
boarding('sample2.txt')
boarding('input.txt')

#p1 answer is 871