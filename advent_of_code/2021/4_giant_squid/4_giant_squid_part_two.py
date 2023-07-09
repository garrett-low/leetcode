def bingo(filename):
    board_array = []
    drawn_num_list = []
    with open(filename, 'rt', encoding='utf-8') as file:
        first_line = file.readline().strip()
        drawn_num_list = [int(num) for num in first_line.split(',')]
        file.readline() # skip empty blank second line
        
        board_i = 0
        board_array.append([])
        for line in file:
            if line == '\n':
                board_i += 1
                board_array.append([])
                continue
            
            line = line.strip()
            split = [int(num) for num in line.split()]
            board_array[board_i].append(split)
    
    # debug
#     print(drawn_num_list)
#     for board in board_array:
#         for row in board:
#             print(f"{row}")
#         print()
    
    num_boards = len(board_array)
    won_board_idx_set = set()
    for drawn_num in drawn_num_list:
        for board_idx, board in enumerate(board_array):
            for row_num in range(len(board)):
                for col_num in range(len(board[row_num])):
                    if board[row_num][col_num] == drawn_num:
                        board[row_num][col_num] = True
                        bingo = check_bingo(board, row_num, col_num)
                        if bingo == True:
                            won_board_idx_set.add(board_idx)
                            if len(won_board_idx_set) == num_boards:                            
                                print_output(board, drawn_num)
                                return
    # debug
#     print(drawn_num_list)
#     for board in board_array:
#         for row in board:
#             print(f"{row}")
#         print()

# diag_one = {(0,0), (1,1), (2,2), (3,3), (4,4)}
# diag_two = {(0,4), (1,3), (2,2), (3,1), (4,0)}
def check_bingo(board, row_num, col_num):
    # diagonals don't count!!!
#     test_coord = (row_num, col_num)
#     if test_coord in diag_one:
#         is_bingo = True
#         for diag_coord in diag_one:
#             row, col = diag_coord
#             if board[row][col] != True:
#                 is_bingo = False
#                 break
#         if is_bingo == True:
#             return is_bingo
#     elif test_coord in diag_two:
#         is_bingo = True
#         for diag_coord in diag_one:
#             row, col = diag_coord
#             if board[row][col] != True:
#                 is_bingo = False
#                 break
#         if is_bingo == True:
#             return is_bingo
    
    # check horizontal
    is_bingo = True
    for col in range(0, 5):
        if board[row_num][col] != True:
            is_bingo = False
            break
    if is_bingo == True:
        return is_bingo
    # check vertical
    is_bingo = True
    for row in range(0, 5):
        if board[row][col_num] != True:
            is_bingo = False
            break
    if is_bingo == True:
        return is_bingo
    
    return False

def print_output(board, drawn_num):
    unmarked_sum = 0
    for row in range(0, 5):
        for col in range(0, 5):
            val = board[row][col]
            if val != True:
                unmarked_sum += val
    
    print(f"{unmarked_sum * drawn_num}")
    return unmarked_sum * drawn_num

bingo('sample.txt')
bingo('input.txt')
