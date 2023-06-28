class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return  f"[{self.x}, {self.y}]"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

def beacon(filename, lower_bound, upper_bound):
    sensor_list = []
    beacon_list = []
    beacon_set = set()
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            colon_splits = line.split(':')
            sensor_splits = colon_splits[0].split(',')
            beacon_splits = colon_splits[1].split(',')
            sensor_x = int(sensor_splits[0].split('x=')[1])
            sensor_y = int(sensor_splits[1].split('y=')[1])
#             print(f"[{sensor_x}, {sensor_y}]")
            beacon_x = int(beacon_splits[0].split('x=')[1])
            beacon_y = int(beacon_splits[1].split('y=')[1])
            sensor_list.append(point(sensor_x, sensor_y))
            beacon_list.append(point(beacon_x, beacon_y))
            beacon_set.add(point(beacon_x, beacon_y))
    
    dist_list = []
    for i in range(len(sensor_list)):
        dist_x = abs(sensor_list[i].x - beacon_list[i].x)
        dist_y = abs(sensor_list[i].y - beacon_list[i].y)
        dist_list.append(dist_x + dist_y)
    
    valid = False
    test_beacon = None
    for check_x in range(lower_bound, upper_bound + 1, 1):
        if valid == True: # break out of check_x
            break
        for check_y in range(lower_bound, upper_bound + 1, 1):
            test_beacon = point(check_x, check_y)
            if test_beacon in beacon_set: # cannot be at the position of an existing beacon
                continue
            
            valid = True
            for i in range(len(sensor_list)):
                sens_x = sensor_list[i].x
                sens_y = sensor_list[i].y
                dist = dist_list[i]
                test_dist = abs(sens_x - check_x) + abs(sens_y - check_y)
                if test_dist <= dist:
                    valid = False
                    break # in range of beacon, break out of for sensor
            
            if valid == True: # break out of check_y
                break
            
    if valid == True:
        print(test_beacon)
    else:
        print("No valid position found!")
    return

def test_what_is_the_python_abs_fn(num):
    return abs(num)
    
beacon('sample.txt', 0, 20)
# beacon('input.txt', 2000000) #p1

#lower 0, upper 4000000 for p2