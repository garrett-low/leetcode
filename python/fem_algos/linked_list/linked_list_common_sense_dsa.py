class node:
    def __init__(self, val, nxt = None):
        self.val = val
        self.nxt = nxt
    def __str__(self):
        return f"[{self.val}]"

class linked_list:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        retval = "["
        curr = self.head
        while curr:
            retval += str(curr.val)
            
            curr = curr.nxt
            if curr:
                retval += ", "
        
        retval += "]"
        
        return retval
    
    def append(self, val):
        if self.head == None:
            self.head = node(val)
            return
            
        curr = self.head
        while curr.nxt:
            curr = curr.nxt
        curr.nxt = node(val)
    
    def add_i(self, val, i):
        new_node = node(val)
        
        if i == 0:
            new_node.nxt = self.head
            self.head = new_node
            return
        
        curr = self.head
        j = 0
        while j < i - 1:
            j += 1
            curr = curr.nxt
        
        new_node.nxt = curr.nxt
        curr.nxt = new_node
    
    def delete_i(self, i):
        if i == 0:
            self.head = self.head.nxt
            return
        
        curr = self.head
        curr_i = 0
        while curr_i < i - 1:
            curr = curr.nxt
            curr_i += 1
        
        after_node = curr.nxt.nxt
        curr.nxt = after_node
    
    def reverse_me(self):
        if self.head == None:
            return
        
        if self.head.nxt == None:
            return
        
        prev = None
        curr = self.head
        while curr:
            temp_nxt = curr.nxt
            curr.nxt = prev
            
            prev = curr
            curr = temp_nxt
        
        self.head = prev

test = linked_list()
test.append(69)
print(test)
test.append(420)
print(test)
test.add_i(350, 0)
print(test)
test.add_i(55, 1)
print(test)
test.add_i(77, 3)
print(test)
test.add_i(421, 5)
print(test)
test.delete_i(0)
print(test)
test.delete_i(1)
print(test)
test.delete_i(3)
print(test)
print("REVERSE ME")
test.reverse_me()
print(test)