DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
    ]

START = (0, 0)

def chiton(filename):
    chiton_map = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            chiton_map.append([int(x) for x in line.strip()])
    
    prev_dict = {}
    dist_dict = {}
    unvisited_min_heap = min_heap()
    for row in len(chiton_map):
        for col in len(chiton_map[0]):
            
            
    end_row = len(chiton_map) - 1
    end_col = len(chiton_map[0]) - 1
class node:
    def __init__(self, prio, val):
        self.prio = prio
        self.val = val
    def __str__(self):
        return f"[{self.prio}: {self.val}]"
        
class min_heap:
    def __init__(self):
        self.arr = []
    def __str__(self):
        retval = ""
        for i in range(len(self.arr)):
            retval += f"{self.arr[i]}"
        return retval
    
    @staticmethod
    def get_left(i):
        return (2 * i) + 1
    @staticmethod
    def get_right(i):
        return (2 * i) + 2
    @staticmethod
    def get_parent(i):
        return (i - 1) // 2
    
    def add(self, prio, val):
        self.arr.append(node(prio, val))
        self.bubble_up(len(self.arr) - 1)
    
    def bubble_up(self, curr_idx):
        par_idx = min_heap.get_parent(curr_idx)
        if par_idx < 0:
            return
        parent = self.arr[par_idx]
        curr = self.arr[curr_idx]
        if parent.prio > curr.prio:
            self.arr[curr_idx] = parent
            self.arr[par_idx] = curr
            self.bubble_up(par_idx)
        return
    
    def remove(self):
        if len(self.arr) == 0:
            print("Nothing to remove!")
            return None
        if len(self.arr) == 1:
            return self.arr.pop()
        
        head = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.bubble_down(0)
        
        return head
    
    def bubble_down(self, curr_idx):
        left_idx = min_heap.get_left(curr_idx)
        if left_idx >= len(self.arr):
            return
        curr = self.arr[curr_idx]
        left = self.arr[left_idx]
        if left.prio < curr.prio:
            self.arr[curr_idx] = left
            self.arr[left_idx] = curr
            self.bubble_down(left_idx)
            return
        right_idx = min_heap.get_right(curr_idx)
        if right_idx >= len(self.arr):
            return
        right = self.arr[right_idx]
        if right.prio < curr.prio:
            self.arr[curr_idx] = right
            self.arr[right_idx] = curr
            self.bubble_down(right_idx)
        
chiton('sample.txt')

heap = min_heap()
heap.add(13, "thirteen")
heap.add(5, "five")
heap.add(25, "twenty-five")
heap.add(12, "twelve")
heap.add(1, "one")
print(heap)
print(heap.remove())
print(heap)
print(heap.remove())
print(heap)
print(heap.remove())
print(heap)
print(heap.remove())
print(heap)
print(heap.remove())
print(heap)
print(heap.remove())
print(heap)