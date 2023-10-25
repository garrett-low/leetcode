START = (0, 0)
WAY_START = (-1,10)

def rain_risk(filename):
    curr_pos = START
    way_rel_pos = WAY_START
    # print(f'START: {curr_pos}, {way_rel_pos}')
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            action = line[0]
            value = int(line[1:])
            
            # print(f'{action} {value}')
            
            way_rel_pos_row, way_rel_pos_col = way_rel_pos
            curr_row, curr_col = curr_pos
            if action == 'L' or action == 'R':
                # the if statements below are for rotating Right
                if action == 'L':
                    if value == 90:
                        value = 270
                    elif value == 270:
                        value = 90
                
                # draw this out and it's straightforward
                if value == 90:
                    way_rel_pos_row, way_rel_pos_col = way_rel_pos_col, way_rel_pos_row
                    way_rel_pos_col *= -1
                elif value == 180:
                    way_rel_pos_row *= -1
                    way_rel_pos_col *= -1
                elif value == 270:
                    way_rel_pos_row, way_rel_pos_col = way_rel_pos_col, way_rel_pos_row
                    way_rel_pos_row *= -1
                
                way_rel_pos = way_rel_pos_row, way_rel_pos_col
                # print(f'  Rotated waypoint to {way_rel_pos}')
            
            if action == 'N' or action == 'E' or action == 'S' or action == 'W':
                if action == 'N':
                    way_rel_pos_row -= value
                elif action == 'E':
                    way_rel_pos_col += value
                elif action == 'S':
                    way_rel_pos_row += value
                else:
                    way_rel_pos_col -= value
                
                way_rel_pos = way_rel_pos_row, way_rel_pos_col
                # print(f'  Relative waypoint: {way_rel_pos}')
            
            if action == 'F':
                # print(f'  Moving from {curr_pos} to {way_rel_pos} x {value}')
                curr_row += way_rel_pos_row * value
                curr_col += way_rel_pos_col * value
                curr_pos = (curr_row, curr_col)
            
            # print(f'  {curr_pos}, {way_rel_pos}')
    print(f'P2: {abs(curr_pos[0]) + abs(curr_pos[1])}')

rain_risk('sample.txt')
rain_risk('input.txt')
rain_risk('input2.txt')
rain_risk('input3.txt')