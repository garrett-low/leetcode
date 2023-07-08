class node:
    def __init__(self, element, prio):
        self.element = element
        self.prio = prio
    def __str__(self):
        return f"[{self.element}: {self.prio}]"

class min_heap:
    def __init__(self):
        self.arr = []
        self.length = 0
        # TODO: implement declaring heap with given list (heapify)
    
    def __str__(self):
        retval = ""
        for item in self.arr:
            retval += f"[{item.element}: {item.prio}]"
        return retval
    
    def __len__(self):
        return self.length
    
    def is_empty(self):
        return self.length == 0
    
    # return min value at root
    # O(1)
    def peek(self):
        if self.is_empty():
            return None
        return self.arr[0]
    
    # add val, maintaining heap rule
    # O(log n)
    def add(self, element, prio):
        new_node = node(element, prio)
        self.arr.append(new_node)
        self.length += 1
        self.bubble_up(self.length - 1)
    
    # inner recursive helper for add
    def bubble_up(self, idx):
        if idx <= 0:
            return
        
        parent_idx = min_heap.get_parent_idx(idx)
        if self.arr[parent_idx].prio <= self.arr[idx].prio:
            return
        # swap and bubble_up
        temp = self.arr[idx]
        self.arr[idx] = self.arr[parent_idx]
        self.arr[parent_idx] = temp
        self.bubble_up(parent_idx)
    
    # remove and return min value (root), maintain heap rule
    # O(log n)
    def remove(self):
        if self.is_empty():
            return None
        root_val = self.arr[0]
        
        self.length -= 1
        
        if self.length == 0:
            self.arr.pop()
            return root_val.element
        
        self.arr[0] = self.arr.pop()
        self.bubble_down(0)
        
        return root_val.element
    
    # inner recursive helper for remove
    def bubble_down(self, idx):
        if min_heap.get_left_idx(idx) >= self.length: # already decremented length
            return
        # find min child and swap if lower
        if min_heap.get_right_idx(idx) >= self.length: # already decremented length
            min_idx = (2 * idx) + 1
        else:
            left = self.arr[min_heap.get_left_idx(idx)].prio
            right = self.arr[min_heap.get_right_idx(idx)].prio
            if left < right:
                min_idx = min_heap.get_left_idx(idx)
            else:
                min_idx = min_heap.get_right_idx(idx)
        
        if self.arr[min_idx].prio >= self.arr[idx].prio:
            return
        # swap and bubble_down
        temp = self.arr[idx]
        self.arr[idx] = self.arr[min_idx]
        self.arr[min_idx] = temp
        self.bubble_down(min_idx)
    
    def update(self, element_to_update, new_prio):
        new_node = node(element_to_update, new_prio)
        found_idx = -1
        for idx in range(len(self.arr)):
            if self.arr[idx].element == element_to_update:
                found_idx = idx
                break
            
        if found_idx == -1:
            print("Element does not exist!")
            return
        
        old_prio = self.arr[idx].prio
        self.arr[idx] = new_node
        if new_prio < old_prio:
            self.bubble_up(idx)
        else:
            self.bubble_down(idx)

    
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
    heap = min_heap()
    heap.add('fifty', 50)
    heap.add('hundo', 100)
    heap.add('twentyfive', 25)
    heap.add('one hundo twenty five', 125)
    heap.add('one hundo fifty', 150)
    print(heap.peek())
    heap.add('one', 1)
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
