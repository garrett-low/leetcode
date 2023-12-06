def boat_race(filename):
    races = {}
    with open(filename, 'rt') as file:
        line_zero = file.readline().strip()
        times_string = line_zero.split(':')[1]
        times = [int(x) for x in times_string.split()]
        
        line_one = file.readline().strip()
        dist_string = line_one.split(':')[1]
        dists = [int(x) for x in dist_string.split()]
        
    for i in range(len(times)):
        races[times[i]] = dists[i]
    # print(times)
    # print(dists)
    # print(races)
    
    ways_to_win = []
    for time in times:
        count_wins = 0
        exp_dist = races[time]
        
        for i in range(time + 1):
            speed = i
            time_remaining = time - i
            my_dist = speed * time_remaining
            
            if my_dist > exp_dist:
                count_wins += 1
        
        ways_to_win.append(count_wins)
    
    result = 1
    for count in ways_to_win:
        result *= count
    print(result)

boat_race('sample.txt')
boat_race('input.txt')

def p2(filename):
    with open(filename, 'rt') as file:
        line_zero = file.readline().strip()
        times_string = line_zero.split(':')[1]
        times = [str(x) for x in times_string.split()]
        
        line_one = file.readline().strip()
        dist_string = line_one.split(':')[1]
        dists = [str(x) for x in dist_string.split()]
    
    concat_time = ""
    for time in times:
        concat_time += time
    
    concat_dist = ""
    for dist in dists:
        concat_dist += dist
    
    time = int(concat_time)
    exp_dist = int(concat_dist)
    
    lower_hold_button_win = 0
    for i in range(time + 1):
        speed = i
        time_remaining = time - i
        my_dist = speed * time_remaining
        
        if my_dist > exp_dist:
            break
        
        lower_hold_button_win += 1
    
    upper_hold_button_win = time - lower_hold_button_win
    ways_to_win = upper_hold_button_win - lower_hold_button_win + 1
    
    print(ways_to_win)

p2('sample.txt')
p2('input.txt')