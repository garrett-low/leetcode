def bingo(filename):
    board_array = []
    drawn_num_list = []
    with open(filename, 'rt', encoding='utf-8') as file:
        first_line = file.readline().strip()
        drawn_num_list = first_line.split(',')
        file.readline() # skip empty blank second line
        
        board_i = 0
        board_array.append([])
        for line in file:
            if line == '\n':
                board_i += 1
                board_array.append([])
                continue
            
            line = line.strip()
            split = line.split(' ')
            board_array[board_i].append(split)
      
    print(drawn_num_list)
    for board in board_array:
        for row in board:
            for col in board:
                print(f"{col} ")
            print()
        print()
        print()
    
bingo('sample.txt')