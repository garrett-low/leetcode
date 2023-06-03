# ring buffer
class RingBuffer:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.length = 0
    
    def __str__(self):
        if self.length == 0:
            return "RB:\t\tI'm empty!"
        
        retval = "RB:\t\t"
        for i in range(self.head, self.head + self.length):
            val = self.array[i % self.capacity]
            retval += f"[{val}]"
        return retval
        
    def add_tail(self, val):
        if self.length >= self.capacity:
            print("RB:\t\tI'm full!")
            return
        
        index = (self.head + self.length) % self.capacity
        self.array[index] = val
        self.length += 1
    
    def peek_tail(self):
        if self.length <= 0:
            print("RB:\t\tI'm empty!")
            return
        index = (self.head + self.length - 1) % self.capacity
        print(f"RB tail:\t[{self.array[index]}]")
    
    def remove_tail(self):
        if self.length <= 0:
            print("RB:\t\tI'm empty!")
            return None
        
        index = (self.head + self.length - 1) % self.capacity
        val = self.array[index]
        self.array[index] = None
        self.length -= 1
        return val
    
    def add_head(self, val):
        if self.length >= self.capacity:
            print("RB:\t\tI'm full!")
            return
        
        self.head = (self.head - 1) % self.capacity
        index = (self.head) % self.capacity
        self.array[index] = val
        self.length += 1
        
    def peek_head(self):
        if self.length <= 0:
            print("RB:\t\tI'm empty!")
            return
        print(self.array[self.head])
    
    def remove_head(self):
        if self.length <= 0:
            print("RB:\t\tI'm empty!")
            return None
        val = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.length -= 1
        return val

def main():
    buf = RingBuffer(5)
    print(buf)
    buf.peek_tail()
    buf.remove_tail()
    buf.add_tail(1)
    buf.peek_tail()
    print(buf)
    buf.add_tail(2)
    buf.peek_tail()
    print(buf)
    buf.add_tail(3)
    buf.peek_tail()
    print(buf)
    buf.add_tail(4)
    buf.peek_tail()
    print(buf)
    buf.remove_tail()
    print(buf)
    buf.add_head(0)
    buf.add_head(-1)
    print(buf)
    buf.add_head("fails")
    buf.remove_tail()
    buf.remove_head()
    print(buf)
    print("\n\nNew test:")
    buf2 = RingBuffer(69)
    for i in range(31):
        buf2.add_tail(i)
    print(buf2)
    for i in range(10,421):
        buf2.add_tail(i)
        buf2.remove_head()
        if i % 10 == 0:
            print(buf2)
    
if __name__ == "__main__":
    main()