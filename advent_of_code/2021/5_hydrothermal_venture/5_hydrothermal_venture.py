class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

def vents(filename):
    with open(filename, 'rt', encoding='utf-8') as file:
        count_dict = {}
        for line in file:
            pair = [x.strip() for x in line.split(' -> ')]
            start = pair[0].split(',')
            end = pair[1].split(',')
            x_start = int(start[0])
            y_start = int(start[1])
            x_end = int(end[0])
            y_end = int(end[1])
            
            if x_start == x_end:
                increment = 1
                if y_end < y_start:
                    increment = -1
                for i in range(y_start, y_end, increment):
                    new_point = point(x_start, i)
                    if new_point in count_dict:
                        count_dict[new_point] += 1
                    else:
                        count_dict[new_point] = 1
                new_point = point(x_start, y_end)
                if new_point in count_dict:
                    count_dict[new_point] += 1
                else:
                    count_dict[new_point] = 1
            
            if y_start == y_end:
                increment = 1
                if x_end < x_start:
                    increment = -1
                for i in range(x_start, x_end, increment):
                    new_point = point(i, y_start)
                    if new_point in count_dict:
                        count_dict[new_point] += 1
                    else:
                        count_dict[new_point] = 1
                new_point = point(x_end, y_start)
                if new_point in count_dict:
                    count_dict[new_point] += 1
                else:
                    count_dict[new_point] = 1
    
    count_overlap = 0
    for key in count_dict:
        if count_dict[key] >= 2:
            count_overlap += 1
    
    print(count_overlap)
    return count_overlap

def draw_line(count_dict, x, y):
    new_point = point(x, y)
    if new_point in count_dict:
        count_dict[new_point] += 1
    else:
        count_dict[new_point] = 1

vents('sample.txt')
vents('input.txt')