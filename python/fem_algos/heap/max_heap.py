class max_heap:
    def __init__(self, cap):
        self.cap = cap
        self.arr = [None] * cap
        self.length = 0
    def __str__(self):
        retval = ""
        for item in self.arr:
            retval += f"[{item}]"
        retval += "\n"
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
        pass
    
    def bubble_down(self, idx):
        pass
    
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

# forgot base case for bubble_up of quitting once we're at arr[0]