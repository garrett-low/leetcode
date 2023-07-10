class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

def vents(filename, is_part_two = False):
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
            
            x_diff = abs(x_start - x_end)
            y_diff = abs(y_start - y_end)
            
            # vertical
            if x_start == x_end:
                increment = 1
                if y_end < y_start:
                    increment = -1
                for i in range(y_start, y_end, increment):
                    draw_line(count_dict, x_start, i)
                draw_line(count_dict,x_start, y_end)
            
            # horizontal
            elif y_start == y_end:
                increment = 1
                if x_end < x_start:
                    increment = -1
                for i in range(x_start, x_end, increment):
                    draw_line(count_dict, i, y_start)
                draw_line(count_dict, x_end, y_start)
                
            # diagonal
            elif x_diff == y_diff and is_part_two:
                x_inc = 1
                if x_end < x_start:
                    x_inc = -1
                y_inc = 1
                if y_end < y_start:
                    y_inc = -1
                y = y_start
                for x in range(x_start, x_end, x_inc):                    
                    draw_line(count_dict, x, y)
                    y += y_inc
                draw_line(count_dict, x_end, y_end)
    
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
vents('sample.txt', True)
vents('input.txt', True)