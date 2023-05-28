class Node:
    def __init__(self, val, nx = None):
        self.val = val
        self.nx = nx

class Queue:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    def __str__(self):
        if self.head == None:
            if self.tail != None:
                return "printout: Q should be empty but you forgot to delete Tail!"
            return "printout: Q is empty!"
        
        retval = f"printout: Head: {self.head.val}, Tail: {self.tail.val}\n"
        retval += "\tQ: "
        curr = self.head
        while curr != None:
            retval += f"[{curr.val}]"
            curr = curr.nx
            
        return retval
        
    def enqueue(self, val):
        new_node = Node(val)
        
        if self.head == None:
            self.head = new_node
        else:
            self.tail.nx = new_node
        
        self.tail = new_node
        print(f"enqueue: {val}")
        
    def dequeue(self):
        print("dequeue: ", end='')
        if self.head == None:
            print("Q is empty!")
            return None
        
        old_head = self.head
        self.head = self.head.nx
        old_head.nx = None
        
        if self.head == None:
            self.tail = None
        
        print(old_head.val)
        return old_head.val
    
    def peek(self):
        print("peek: ", end='')
        if self.head == None:
            return "Q is empty!"
        return self.head.val

def main():
    testq = Queue()
    print(testq)
    print(testq.peek())
    testq.dequeue()
    testq.enqueue(69)
    print(testq.peek())
    print(testq)
    testq.enqueue(420)
    print(testq.peek())
    print(testq)
    testq.enqueue(42069)
    print(testq.peek())
    print(testq)
    testq.dequeue()
    print(testq)
    print(testq.peek())
    testq.dequeue()
    print(testq)
    print(testq.peek())
    testq.dequeue()
    print(testq)
    print(testq.peek())
    testq.dequeue()
    print(testq)
    print(testq.peek())
    
if __name__ == "__main__":
    main()