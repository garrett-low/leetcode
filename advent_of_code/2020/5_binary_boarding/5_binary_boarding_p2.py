import sys

ROW_MAX = 127
COL_MAX = 7

def boarding(filename):
    seats = set()
    max_seat_id = 0
    min_seat_id = sys.maxsize
    
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            line = line.strip()
            row_search = line[:7]
            col_search = line[7:]
            
            row_id = partition(row_search, 0, ROW_MAX)
            col_id = partition(col_search, 0, COL_MAX)
            seat_id = row_id * 8 + col_id
            seats.add(seat_id)
            if seat_id > max_seat_id:
                max_seat_id = seat_id
            if seat_id < min_seat_id:
                min_seat_id = seat_id
    
    # print(seats)
    # sorted_seats = merge_sort(seats)
    # print(sorted_seats)
    
    for test_id in range(min_seat_id, max_seat_id + 1):
        if test_id not in seats:
            print(test_id)
            return

def partition(bsp_string, lo, hi):
    for ch in bsp_string:
        mid = ((hi - lo) // 2) + lo
        if ch == 'F' or ch == 'L':
            hi = mid
        else:
            lo = mid + 1
    
    return lo

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    arr_left = merge_sort(arr[:mid])
    arr_right = merge_sort(arr[mid:])
    
    return merge(arr_left, arr_right)

def merge(arr_left, arr_right):
    sorted = []
    i = 0
    j = 0
    
    while i < len(arr_left) and j < len(arr_right):
        left = arr_left[i]
        right = arr_right[j]
        if left < right:
            sorted.append(left)
            i += 1
        else:
            sorted.append(right)
            j += 1
    
    sorted.extend(arr_left[i:])
    sorted.extend(arr_right[j:])
    
    return sorted

# print(partition('FBFBBFF', 0, 127))
# boarding('sample1.txt')
# boarding('sample2.txt')
boarding('input.txt')

#p1 answer is 871