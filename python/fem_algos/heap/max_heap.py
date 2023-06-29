class max_heap:
    def __init__(self, cap):
        self.cap = cap
        self.arr = [None] * cap
        self.length = 0
        
    def __str__(self):
        retval = ""
        for item in self.arr:
            retval += f"[{item}]"
        return retval
    
    def add(self, val):
        if self.length >= self.cap:
            print("I'm full!")
            return
        
        if self.length == 0:
            self.arr[0] = val
            self.length += 1
            return
        
        self.arr[self.length] = val
        self.bubble_up(self.length, val)
        self.length += 1
    def bubble_up(self, idx, val):
        parent_idx = max_heap.get_parent(idx)
        parent = self.arr[parent_idx]
        if val < parent:
            return
        if idx == 0:
            return
        
        self.arr[parent_idx] = val
        self.arr[idx] = parent
        self.bubble_up(parent_idx, val)
        
    def peek(self):
        if self.length <= 0:
            print("I'm empty!")
            return None
        print(self.arr[0])
        return self.arr[0]
    
    def remove(self):
        if self.length <= 0:
            print("I'm empty!")
            return None
        
#         print(f"Removing: {self.arr[0]}")
        retval = self.arr[0]
        self.arr[0] = self.arr[self.length - 1]
        self.arr[self.length - 1] = None
        self.length -= 1
        self.bubble_down(0)
        
        return retval
    
    def bubble_down(self, idx):
        if idx >= self.length - 1:
            return
        left_idx = heap.get_left(idx)
        if left_idx >= self.length - 1: # no children
            return
        
        curr = self.arr[idx]
        right_idx = heap.get_right(idx)
        swap_idx = - 1
        if curr < self.arr[left_idx]:
            swap_idx = left_idx
        elif right_idx <= self.length - 1 and curr < self.arr[right_idx]:
            swap_idx = right_idx
        else:
            return
        
        self.arr[idx] = self.arr[swap_idx]
        self.arr[swap_idx] = curr
        self.bubble_down(swap_idx)
    
    @staticmethod
    def get_parent(index):
        return index // 2;
    @staticmethod
    def get_left(index):
        return 2 * index + 1
    @staticmethod
    def get_right(index):
        return 2 * index + 2

heap = max_heap(5)
heap.add(5)
print(heap)
heap.add(50)
heap.add(70)
heap.add(420)
heap.add(69)
print(heap)
heap.peek()
heap.add(120)
heap.remove()
print(heap)
heap.remove()
print(heap)
heap.remove()
print(heap)
heap.remove()
print(heap)
heap.remove()
print(heap)
heap.remove()

# forgot base case for bubble_up of quitting once we're at arr[0]