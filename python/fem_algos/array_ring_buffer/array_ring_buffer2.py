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
        index = (self.head + self.length - 1) % self.capacity
        print(f"RB tail:\t[{self.array[index]}]")
    
    def remove_tail(self):
        pass

def main():
    buf = RingBuffer(5)
    print(buf)
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
    
if __name__ == "__main__":
    main()