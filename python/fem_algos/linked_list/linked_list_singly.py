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
        
# test
def main():
    ll = LinkedList()
    print("Length: ", ll.get_length())
    print(ll.get_val(69))
    print(ll.remove_val(-1))
    ll.append(69)
    print(ll)
    print(ll.get_val(69))
    ll.append(68)
    print(ll)
    ll.append(420)
    print(ll)
    ll.prepend(-1)
    print(ll)
    print("Length: ", ll.get_length())
    print(ll.get_val(-1))
    print(ll.get_val(69))
    print(ll.get_val(420))
    print(ll.remove_val(420))
    print(ll)
    print(ll.remove_val(420))
    print(ll)
    print(ll.remove_val(-1))
    print(ll)
    print(ll.remove_val(68))
    print(ll)
    print(ll.remove_val(69))
    print(ll)
    print("\n")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll)
    print(ll.remove_at(1))
    print(ll)
    ll.append(4)
    print(ll)
    print(ll.remove_at(2))
    print(ll)
    print(ll.remove_at(2))
    print(ll)
    print(ll.remove_at(0))
    print(ll)
    print(ll.remove_at(0))
    print(ll)
    print(ll.insert_at(69,1))
    print(ll)
    print(ll.insert_at(69,0))
    print(ll)
    print(ll.insert_at(420,1))
    print(ll)
    print(ll.insert_at(70,1))
    print(ll)
    print(ll.insert_at(421,3))
    print(ll)
    print(ll.get_at(0))
    print(ll.get_at(1))
    print(ll.get_at(2))
    print(ll.get_at(3))
    print(ll.get_at(4))

if __name__ == "__main__":
    main()