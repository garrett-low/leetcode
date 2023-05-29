# ring buffer without resizing
# aka circular buffer aka circular queue aka cyclic buffer aka ring buffer
# start inclusive, end exclusive - self.head is the index containing an element
# double-ended queue operations

class RingBuffer:
    def __init__(self, capacity):
        self.head = 0
        self.length = 0
        self.capacity = capacity
        self.array = [None] * capacity
        
    def __str__(self):
        retval = "Contents:\t\t"
        if self.length == 0:
            retval += "RingBuffer is empty!"
        else:
            retval += f"Head: {self.head}, Length: {self.length}, Capacity: {self.capacity}\nBuf:\t\t\t"
            for i in range(self.length):
                index = (i + self.head) % self.capacity
                retval += f"[{self.array[index]}]"
            retval += "\nArr:\t\t\t"
            for i in range(self.capacity):
                retval += f"[{self.array[i]}]"
                
        return retval
    
    def push_back(self, val): # add after tail 
        if self.length >= self.capacity:
            return
        index = (self.head + self.length) % self.capacity
        self.array[index] = val
        self.length += 1
    
    def pop_back(self): # take from tail
        if self.length == 0:
            return None
        index = (self.head + self.length - 1) % self.capacity
        retval = self.array[index]
        self.array[index] = None # optional
        self.length -= 1
        return retval
    
    def push_front(self, val): # add before head
        if self.length >= self.capacity:
            return
        index = abs((self.head - 1) % self.capacity)
        self.array[index] = val
        self.length += 1
        self.head = index
        
    def pop_front(self): # take from head
        if self.length == 0:
            return None
        retval = self.array[self.head]
        self.array[self.head] = None # optional
        self.length -= 1
        self.head = abs((self.head + 1) % self.capacity)
        return retval
    
def main():
    buf = RingBuffer(5)
    print(buf)
    buf.pop_front()
    buf.pop_back()
    buf.push_front(1)
    print(buf)
    buf.pop_front()
    print(buf)
    buf.push_back(2)
    print(buf)
    buf.pop_back()
    print(buf)
    buf.push_front(1)
    buf.push_front(2)
    buf.push_front(3)
    buf.push_front(4)
    buf.push_front(5)
    print(buf)
    buf.push_front(6)
    print(buf)
    buf.pop_back()
    print(buf)
    buf.pop_back()
    print(buf)
    buf.pop_back()
    print(buf)
    buf.pop_back()
    print(buf)
    buf.pop_back()
    print(buf)
    buf.push_back("a")
    print(buf)
    buf.push_back("b")
    print(buf)
    buf.push_back("c")
    print(buf)
    for i in range(100, 123, 1):
        buf.push_back(chr(i))
        print(buf)
        buf.pop_front()
        print(buf)
    for i in range(122, 96, -1):
        buf.push_front(chr(i))
        print(buf)
        buf.pop_back()
        print(buf)
    
if __name__ == "__main__":
    main()