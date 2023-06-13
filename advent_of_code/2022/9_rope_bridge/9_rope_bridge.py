#4532 - bad hash function
#6347 - better hash function, still too low

# import hashlib
# import collections

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"[{self.x},{self.y}]"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
#         return self.x + self.y
        return hash((self.x, self.y))
#         m = hashlib.sha256()
#         m.update(self.x.to_bytes(32, byteorder='big'))
#         m.update(self.y.to_bytes(32, byteorder='big'))
#         return m.digest()
#         return hash(((self.x + self.y) * (self.x + self.y + 1)/2) + self.y)

class Head:
    def __init__(self):
        self.pt = Point(0, 0)

class Tail:
    def __init__(self):
        self.pt = Point(0, 0)
        self.visited_set = set()
        self.visited_list = list()
#         self.visited_list = LinkedList()

def count_tail_visited(filename):
    h = Head()
    t = Tail()
    t.visited_set.add(t.pt) # add 0,0
#     print(len(t.visited_set))
#     print(f"Head: {h.pt}, Tail: {t.pt}")
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            move = line.split(' ')
            move_dir = move[0]
            move_steps = int(move[1])
#             print(f"{move_dir} {move_steps}")
            for _ in range(0, move_steps):
                move_head(move_dir, h)                
                move_tail(h, t)
                t.visited_set.add(t.pt)
                t.visited_list.append(t.pt)
#                 print(f"Head: {h.pt}, Tail: {t.pt}")
    
#     i = 0
#     for _ in t.visited_set:
#         i += 1
    unique_list = list()
    for point in t.visited_list:
        if point not in unique_list:
            unique_list.append(point)
#     for i in range(0, t.visited_list.get_length()):
#         for j in range(0, t.visited_list.get_length()):
#             if i == j:
#                 continue
#             if t.visited_list.get_at(i) == t.visited_list.get_at(j):
#                 t.visited_list.remove_at(j)
    
#     print(t.visited_list.get_length())
    
    print(len(t.visited_list))
    print(len(unique_list))
    print(len(t.visited_set))
    return

def move_head(move_dir, h):
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

class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next_node = next_node
         
class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    def __str__(self):
        if self.head == None:
            if self.tail != None:
                return "LL is empty but you forgot to delete Tail!"
            return "Linked List is empty!"
        
        ll = f"Head: {self.head.val}\n"
        ll += f"Tail: {self.tail.val}\n"
        
        ll += "Linked List: "
        curr = self.head
        while curr != None:
            ll += f"[{curr.val}]"
            curr = curr.next_node
        
        return ll
    
    def append(self, new_val):
        new_node = Node(new_val)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            curr = self.head
            
            while curr.next_node != None:
                curr = curr.next_node
                
            curr.next_node = new_node
            self.tail = new_node
            
    def prepend(self, new_val):
        new_node = Node(new_val)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
    
    def get_length(self):
        i = 0
        curr = self.head
        while curr != None:
            curr = curr.next_node
            i += 1
        return i
    
    def get_val(self, val):
        i = 0
        curr = self.head
        
        while curr != None:
            if curr.val == val:
                return f"get_val: Found {val} at Node {i}"
            curr = curr.next_node
            i += 1
        
        return "get_val: Not found"
    
    def get_at(self, index):
        i = 0
        curr = self.head
        
        while i < index and curr != None:
            curr = curr.next_node
            i += 1
        
        if curr == None:
            print("Error: index DNE!")
            return None
        
        return curr.val
    
    def remove_val(self, val):
        if self.head == None:
            return "remove_val: Empty list"
        
        if self.head.val == val:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next_node
            return f"remove_val: Removed {val} at Head"
        
        curr = self.head
        i = 1
        while curr.next_node != None:
            if curr.next_node.val == val:
                if self.tail == curr.next_node:
                    self.tail = curr
                curr.next_node = curr.next_node.next_node
                return f"remove_val: Removed {val} at Node {i}"
                
            curr = curr.next_node
            i += 1
        
        return "remove_val: Not found"
    
    def remove_at(self, index):
        removed_val = -1
        
        if self.head == None:
            return "remove_at: Empty list"
        
        if index == 0:
            removed_val = self.head.val
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next_node
            return f"remove_at: Removed {removed_val} at Head"
            
        curr = self.head
        i = 1
        while curr.next_node != None:
            if i == index:
                removed_val = curr.next_node.val
                if self.tail == curr.next_node:
                    self.tail = curr
                curr.next_node = curr.next_node.next_node
                return f"remove_at: Removed {removed_val} at Node {index}"
            curr = curr.next_node
            i += 1
        
        return f"remove_at: Node {index} does not exist"
    
    def insert_at(self, val, index):
        new_node = Node(val)
        
        if index == 0:
            if self.head == None:
                self.tail = new_node
            else:
                new_node.next_node = self.head
            
            self.head = new_node
            return f"insert_at: Inserted {val} at Head"
        
        curr = self.head
        i = 1
        while curr != None:
            if i == index:
                new_node.next_node = curr.next_node
                curr.next_node = new_node
                if curr == self.tail:
                    self.tail = new_node
                return f"insert_at: Inserted {val} at Node {index}"
            
            curr = curr.next_node
            i += 1
        
        return f"insert_at: Node {index} does not exist"

count_tail_visited("input_sample.txt")
count_tail_visited("input.txt")