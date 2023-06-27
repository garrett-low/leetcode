import sys

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

def beacon(filename, check_y):
    sensor_list = []
    beacon_list = []
    beacon_set = set()
    max_x = 0
    min_x = sys.maxsize
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
            if beacon_x > max_x:
                max_x = beacon_x
            if sensor_x > max_x:
                max_x = sensor_x
            if beacon_x < min_x:
                min_x = beacon_x
            if sensor_x < min_x:
                min_x = sensor_x
    
    print(f"min: {min_x}, max: {max_x}")
    
    dist_list = []
    max_dist = 0
    for i in range(len(sensor_list)):
        dist_x = abs(sensor_list[i].x - beacon_list[i].x)
        dist_y = abs(sensor_list[i].y - beacon_list[i].y)
        dist_list.append(dist_x + dist_y)
        if (dist_x + dist_y) > max_dist:
            max_dist = dist_x + dist_y
    
    retnum = 0
    for check_x in range(min_x - max_dist, max_x + max_dist + 1, 1):
        test_beacon = point(check_x, check_y)
        if test_beacon in beacon_set: # cannot be at the position of an existing beacon
            continue
        
        for i in range(len(sensor_list)):
            sens_x = sensor_list[i].x
            sens_y = sensor_list[i].y
            dist = dist_list[i]
#             print(f"check: [{check_x}, {check_y}], sens: [{sens_x}, {sens_y}], dist: {dist}")
            test_dist = abs(sens_x - check_x) + abs(sens_y - check_y)
            if test_dist <= dist:
#                 print(f"invalid: [{check_x}, {check_y}]")
                retnum += 1
                break # in range of beacon, break out of for sensor
    print(retnum)
    return

def test_what_is_the_python_abs_fn(num):
    return abs(num)
    
beacon('sample.txt', 10)
beacon('input.txt', 2000000) #p1

# 3909634 too low
# bounds might be wrong, account for distance away from the first and last sensors
# 4985193 attempt 2

# print(test_what_is_the_python_abs_fn(-1))
# print(test_what_is_the_python_abs_fn(1))