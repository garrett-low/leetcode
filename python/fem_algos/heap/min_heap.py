class MinHeap:
    def __init__(self):
        self.arr = []
        self.length = 0
        # TODO: implement declaring heap with given list (heapify)
    
    def __str__(self):
        retval = ""
        for item in self.arr:
            retval += f"[{item}]"
        return retval
    
    def isEmpty(self):
        return self.length == 0
    
    # return min value at root
    # O(1)
    def peek(self):
        if self.isEmpty():
            return None
        return self.arr[0]
    
    # add val, maintaining heap rule
    # O(log n)
    def add(self, val):
        self.arr.append(val)
        self.length += 1
        self.bubble_up(self.length - 1)
    
    # inner recursive helper for add
    def bubble_up(self, idx):
        if idx <= 0:
            return
        
        parent_idx = MinHeap.get_parent_idx(idx)
        if self.arr[parent_idx] <= self.arr[idx]:
            return
        # swap and bubble_up
        temp = self.arr[idx]
        self.arr[idx] = self.arr[parent_idx]
        self.arr[parent_idx] = temp
        self.bubble_up(parent_idx)
    
    # remove and return min value (root), maintain heap rule
    # O(log n)
    def remove(self):
        if self.isEmpty():
            return None
        root_val = self.arr[0]
        
        self.length -= 1
        
        if self.length == 0:
            self.arr.pop()
            return root_val
        
        self.arr[0] = self.arr.pop()
        self.bubble_down(0)
        
        return root_val
    
    # inner recursive helper for remove
    def bubble_down(self, idx):
        if MinHeap.get_left_idx(idx) >= self.length: # already decremented length
            return
        # find min child and swap if lower
        if MinHeap.get_right_idx(idx) >= self.length: # already decremented length
            min_idx = (2 * idx) + 1
        else:
            left = self.arr[MinHeap.get_left_idx(idx)]
            right = self.arr[MinHeap.get_right_idx(idx)]
            if left < right:
                min_idx = MinHeap.get_left_idx(idx)
            else:
                min_idx = MinHeap.get_right_idx(idx)
        
        if self.arr[min_idx] >= self.arr[idx]:
            return
        # swap and bubble_down
        temp = self.arr[idx]
        self.arr[idx] = self.arr[min_idx]
        self.arr[min_idx] = temp
        self.bubble_down(min_idx)
    
    # more helpers
    @staticmethod
    def get_parent_idx(idx):
        return (idx - 1) // 2
    
    @staticmethod
    def get_left_idx(idx):
        return (2 * idx) + 1
    
    @staticmethod
    def get_right_idx(idx):
        return (2 * idx) + 2

def main():
    heap = MinHeap()
    heap.add(50)
    heap.add(100)
    heap.add(25)
    heap.add(125)
    heap.add(150)
    print(heap.peek())
    heap.add(1)
    print(heap.peek())
    print("remove: " + str(heap.remove()))
    print(heap.peek())
    print(heap)
    print("remove: " + str(heap.remove()))
    print(heap.peek())
    print(heap)
    print("remove: " + str(heap.remove()))
    print(heap.peek())
    print(heap)
    print("remove: " + str(heap.remove()))
    print(heap.peek())
    print(heap)
    print("remove: " + str(heap.remove()))
    print(heap.peek())
    print(heap)
    print("remove: " + str(heap.remove()))
    print(heap.peek())
    print(heap)
    print("remove: " + str(heap.remove()))
    print(heap.peek())
    print(heap)
    
if __name__ == "__main__":
    main()