import sys

rock = 9608
air = 9617
sand = 9679

def falling_sand(filename):    
    min_row = sys.maxsize
    min_col = sys.maxsize
    max_row = sys.maxsize
    max_col = sys.maxsize
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            line_split = line.split(' -> ')
            for i in range(len(line_split) - 1):
                draw_rock(line_split[i], line_split[i + 1])

def draw_rock(point1, point2):
    

def print_test():
    arr = [[air for col in range(10)] for row in range(10)]
    for row in arr:
        for col in row:
            print(chr(col), end='')
        print()

print(chr(rock))
print(chr(air))
print(chr(sand))

falling_sand('sample.txt')