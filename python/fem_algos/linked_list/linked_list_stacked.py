class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next_node = next_node
    
class Stack:
    def __init__(self, head = None, length = 0):
        self.head = head
        self.length = length
    
    def __str__(self):
        if self.head == None:
            return "Stack is empty"
        
        retval = f"printout: Head: {self.head.val}, Length = {self.length}\n"
        retval += "\tStack: "
        curr = self.head
        while curr != None:
            retval += f"[{curr.val}]"
            curr = curr.next_node
        
        return retval
        
    def push(self, val):
        print(f"debug: push: \tPushed {val}")
        new_node = Node(val)
        self.length += 1
        
        new_node.next_node = self.head
        self.head = new_node
        
    def pop(self):
        print("debug: pop: ", end='')
        if self.head == None:
            print("\tStack is empty!")
            return None
        
        old_head = self.head
        self.head = self.head.next_node
        old_head.next = None
        self.length -= 1
        
        print(f"\tPopped {old_head.val}")
        return old_head.val
    
    def peek(self):
        print("debug: peek: ", end='')
        if self.head == None:
            print("\tStack is empty!")
            return None
        print(f"\tPeeked {self.head.val}")
        return self.head.val
            
def main():
    teststack = Stack()
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