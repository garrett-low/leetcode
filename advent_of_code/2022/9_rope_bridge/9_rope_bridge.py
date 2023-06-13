class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"[{self.x},{self.y}]"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash(((self.x + self.y) * (self.x + self.y + 1)/2) + self.y)

class Head:
    def __init__(self):
        self.pt = Point(0, 0)

class Tail:
    def __init__(self):
        self.pt = Point(0, 0)
        self.visited_set = set()

def count_tail_visited(filename):
    h = Head()
    t = Tail()
    t.visited_set.add(t.pt) # add 0,0
#     print(f"Head: {h.pt}, Tail: {t.pt}")
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            move = line.split(' ')
            move_dir = move[0]
            move_steps = int(move[1])
#             print(f"{move_dir} {move_steps}")
            for _ in range(0, move_steps):
                move_head(move_dir, h, t)                
                move_tail(h, t)
                t.visited_set.add(t.pt)
#                 print(f"Head: {h.pt}, Tail: {t.pt}")
                
    print(len(t.visited_set))
    return

def move_head(move_dir, h, t):
    if move_dir == 'U':
        h.pt.y += 1
    elif move_dir == 'R':
        h.pt.x += 1
    elif move_dir == 'D':
        h.pt.y -= 1
    elif move_dir == 'L':
        h.pt.x -= 1
        
def move_tail(h, t):
    # um yeah well this could be more concise with absolute value
    # but that is too clever for my taste
    if t.pt.y + 2 == h.pt.y and t.pt.x == h.pt.x: # up 2
        t.pt.y += 1
    elif t.pt.x + 2 == h.pt.x and t.pt.y == h.pt.y: # right 2
        t.pt.x += 1
    elif t.pt.y - 2 == h.pt.y and t.pt.x == h.pt.x: # down 2
        t.pt.y -= 1
    elif t.pt.x - 2 == h.pt.x and t.pt.y == h.pt.y: # left 2
        t.pt.x -= 1
    # knight moves
    elif t.pt.x + 1 == h.pt.x and t.pt.y + 2 == h.pt.y: # 1 o'clock
        t.pt.x += 1
        t.pt.y += 1
    elif t.pt.x + 2 == h.pt.x and t.pt.y + 1 == h.pt.y: # 2 o'clock
        t.pt.x += 1
        t.pt.y += 1
    elif t.pt.x + 2 == h.pt.x and t.pt.y - 1 == h.pt.y: # 4 o'clock
        t.pt.x += 1
        t.pt.y -= 1
    elif t.pt.x + 1 == h.pt.x and t.pt.y - 2 == h.pt.y: # 5 o'clock
        t.pt.x += 1
        t.pt.y -= 1
    elif t.pt.x - 1 == h.pt.x and t.pt.y - 2 == h.pt.y: # 7 o'clock
        t.pt.x -= 1
        t.pt.y -= 1
    elif t.pt.x - 2 == h.pt.x and t.pt.y - 1 == h.pt.y: # 8 o'clock
        t.pt.x -= 1
        t.pt.y -= 1
    elif t.pt.x - 2 == h.pt.x and t.pt.y + 1 == h.pt.y: # 10 o'clock
        t.pt.x -= 1
        t.pt.y += 1
    elif t.pt.x - 1 == h.pt.x and t.pt.y + 2 == h.pt.y: # 11 o'clock
        t.pt.x -= 1
        t.pt.y += 1
            
count_tail_visited("input_sample.txt")
count_tail_visited("input.txt")