# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next_node = None
    
class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array_list = [None] * capacity
        self.count = 0
    
    def __str__(self):
        if self.count <= 0:
            return "printout:\t\tArrayList is empty!"
        
        retval = f"printout:\t\tCount: {self.count}, Capacity: {self.capacity}\n"
        retval += "\t\t\t"
        for i in range(self.count):
            retval += f"[{self.array_list[i]}]"
            
        return retval
        
    def extend_capacity(self):
#         print("extend_capacity:\t", self.array_list)
        array_list_new = [None] * self.capacity * 2
        
        self.capacity = self.capacity * 2
        for i in range(self.count):
            array_list_new[i] = self.array_list[i]
            
        self.array_list = array_list_new
        print("extend_capacity:\t", self.array_list)
    
    def push(self, val):
        if self.count >= self.capacity:
            self.extend_capacity()
        
        self.array_list[self.count] = val
        self.count += 1
        print(f"push:\t\t\t{val}")
        
    def pop(self):
        print("pop:\t\t\t", end='')
        if self.count <= 0:
            print("ArrayList is empty!")
            return None
        
        popped = self.array_list[self.count - 1]
        self.array_list[self.count - 1] = None # optional
        self.count -= 1
        print(f"{popped}")
        return popped
    
    def peek(self):
        print("peek:\t\t\t", end='')
        if self.count <= 0:
            print("ArrayList is empty!")
            return None
        
        print(f"{self.array_list[self.count - 1]}")
        return self.array_list[self.count - 1]

def main():
    teststack = ArrayList(1)
    print(teststack)
    teststack.peek()
    teststack.pop()
    teststack.push(69)
    teststack.peek()
    print(teststack)
    teststack.push(420)
    teststack.peek()
    print(teststack)
    teststack.push(42069)
    teststack.peek()
    print(teststack)
    teststack.push("weewoo")
    teststack.peek()
    print(teststack)
    teststack.push("woweee")
    teststack.peek()
    print(teststack)
    teststack.pop()
    teststack.peek()
    print(teststack)
    teststack.pop()
    teststack.peek()
    print(teststack)
    teststack.pop()
    teststack.peek()
    print(teststack)
    teststack.pop()
    teststack.peek()
    print(teststack)
    teststack.pop()
    teststack.peek()
    print(teststack)
    teststack.pop()
    teststack.peek()
    print(teststack)
    
if __name__ == "__main__":
    main()