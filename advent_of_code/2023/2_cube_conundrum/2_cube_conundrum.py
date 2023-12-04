BAG_COUNT_DICT = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def cube(filename):
    game_idx = 1
    game_data = []
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            colon_split = line.split(':')
            
            grabs_ary = []
            grabs = colon_split[1]      
            for grab in grabs.split(';'):
                grab = grab.strip()
                grab_dict = {}
                for num_color_pair in grab.split(','):
                    num_color_pair = num_color_pair.strip()
                    num_color_split = num_color_pair.split(' ')
                    
                    num = num_color_split[0]
                    color = num_color_split[1]
                    
                    grab_dict[color] = int(num)
            
                grabs_ary.append(grab_dict)
            
            game_data.append(grabs_ary)
            game_idx += 1
    
    # print(game_data)
    
    p1_calc(game_data)
    p2_calc(game_data)

def p1_calc(game_data):
    invalid_game_set = set()
    valid_game_set = set()
    game_idx = 1
    
    for game in game_data:
        is_valid_game = True
        for grab in game:
            for color in grab:
                test_num = grab[color]
                max_num = BAG_COUNT_DICT[color]
                if test_num > max_num:
                    is_valid_game = False
                    
        if is_valid_game:
            valid_game_set.add(game_idx)
        else:
            invalid_game_set.add(game_idx)
        game_idx += 1
    
    # print(valid_game_set)
    
    result = 0
    for game_id in valid_game_set:
        result += game_id
        
    print(f"P1: {result}")

def p2_calc(game_data):
    result = 0
    for game in game_data:
        power = 0
        
        max_red = 0
        max_green = 0
        max_blue = 0
        for grab in game:
            for color in grab:
                test_num = grab[color]
                match color:
                    case "red":
                        if test_num > max_red:
                            max_red = test_num
                    case "green":
                        if test_num > max_green:
                            max_green = test_num
                    case "blue":
                        if test_num > max_blue:
                            max_blue = test_num
        
        power = max_red * max_green * max_blue
        result += power
        
    print(f"P2: {result}")
                    
cube('sample.txt')
cube('input.txt')