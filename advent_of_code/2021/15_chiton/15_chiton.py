import sys
from collections import deque

NEIGHBOR_DIRS = [
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
    dist_dict[START] = 0
    for row_i in range(len(chiton_map)):
        for col_i in range(len(chiton_map[0])):
            if (row_i, col_i) != START:
                dist_dict[(row_i, col_i)] = sys.maxsize
            prev_dict[(row_i, col_i)] = None
            unvisited_min_heap.add(dist_dict[(row_i, col_i)], (row_i, col_i))
            
    end_row = len(chiton_map) - 1
    end_col = len(chiton_map[0]) - 1
    
    while not unvisited_min_heap.is_empty():
        curr = unvisited_min_heap.remove()
    
        for dirs_tuple in NEIGHBOR_DIRS:
            neighbor_row = dirs_tuple[0] + curr[0]
            neighbor_col = dirs_tuple[1] + curr[1]
            neighbor_tuple = (neighbor_row, neighbor_col)
            if neighbor_col > end_col or neighbor_col < 0:
                continue
            if neighbor_row > end_row or neighbor_row < 0:
                continue
            
            test_dist = dist_dict[curr] + chiton_map[neighbor_row][neighbor_col]
            if test_dist < dist_dict[neighbor_tuple]:
                dist_dict[neighbor_tuple] = test_dist
                prev_dict[neighbor_tuple] = curr
                unvisited_min_heap.update(neighbor_tuple, test_dist)
                
    output_path = deque((end_row, end_col))
    output_risk = dist_dict[(end_row, end_col)] # start with penultimate risk
    curr_pos = prev_dict[(end_row, end_col)]
    while curr_pos != None:
#         print(curr_pos)
        output_path.appendleft(curr_pos)
#         output_risk += dist_dict[curr_pos]
        curr_pos = prev_dict[curr_pos]
    print(output_path)
    print(output_risk)
    
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
    
    def is_empty(self):
        return len(self.arr) <= 0
    
    def add(self, prio, val):
        self.arr.append(node(prio, val))
        self.bubble_up(len(self.arr) - 1)
    
    def bubble_up(self, curr_idx):
        if curr_idx <= 0:
            return
        par_idx = min_heap.get_parent(curr_idx)

        parent = self.arr[par_idx]
        curr = self.arr[curr_idx]
        if parent.prio <= curr.prio:
            return
        
        self.arr[curr_idx] = parent
        self.arr[par_idx] = curr
        self.bubble_up(par_idx)
        return
    
    def remove(self):
        if len(self.arr) == 0:
            print("\tNothing to remove!")
            return None
        if len(self.arr) == 1:
            return self.arr.pop().val
        
        head = self.arr[0].val
        self.arr[0] = self.arr.pop()
        self.bubble_down(0)
        
        return head
    
#     def bubble_down(self, curr_idx):
#         left_idx = min_heap.get_left(curr_idx)
#         if left_idx >= len(self.arr):
#             return
#         curr = self.arr[curr_idx]
#         left = self.arr[left_idx]
#         if left.prio < curr.prio:
#             self.arr[curr_idx] = left
#             self.arr[left_idx] = curr
#             self.bubble_down(left_idx)
#             return
#         right_idx = min_heap.get_right(curr_idx)
#         if right_idx >= len(self.arr):
#             return
#         right = self.arr[right_idx]
#         if right.prio < curr.prio:
#             self.arr[curr_idx] = right
#             self.arr[right_idx] = curr
#             self.bubble_down(right_idx)
    def bubble_down(self, idx):
        if min_heap.get_left(idx) >= len(self.arr): # already decremented length
            return
        # find min child and swap if lower
        if min_heap.get_right(idx) >= len(self.arr): # already decremented length
            min_idx = (2 * idx) + 1
        else:
            left = self.arr[min_heap.get_left(idx)].prio
            right = self.arr[min_heap.get_right(idx)].prio
            if left < right:
                min_idx = min_heap.get_left(idx)
            else:
                min_idx = min_heap.get_right(idx)
        
        if self.arr[min_idx].prio >= self.arr[idx].prio:
            return
        # swap and bubble_down
        temp = self.arr[idx]
        self.arr[idx] = self.arr[min_idx]
        self.arr[min_idx] = temp
        self.bubble_down(min_idx)
    
    def peek(self):
        return self.arr[0]
    
    def update(self, val, new_prio):
        if len(self.arr) == 0:
            print("\tI'm empty!")
            return
        found_i = -1
        for i in range(len(self.arr)):
            if val == self.arr[i].val:
                found_i = i
                break
        
        if found_i == -1:
            print("\tNode val not in heap!")
            return
        
        old_prio = self.arr[found_i].prio
        self.arr[found_i].prio = new_prio
        if old_prio > new_prio:
            self.bubble_up(found_i)
        else:
            self.bubble_down(found_i)
        
chiton('sample.txt')
chiton('input.txt')