# from collections import defaultdict
from collections import deque
from collections import heapq

class node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    def __str__(self):
        return f"[{self.key} : {self.val}]"

class lru_cache:
	def __init__(self, cap):
		self.hashmap = {} # dict val is queue index
        self.queue = deque() # node contains val
        self.cap = cap
        
    def __str__(self):
        retval = "deque: "
        for node in self.queue:
            retval += f"[{node}]"
        retval += f"\nhashmap: {self.hashmap}"
        return retval
        
    def get(self, key):
        if key in self.hashmap:
            return self.hashmap[key]
        
        return -1
    
    def put(self, key, val):
        node_i = self.get(key)
        found_node = self.queue.remove(node_i)
        found_node.val = val
        self.queue.appendleft(found_node)
        
        
        if node_i == -1:
            new_node = node(key, val)
            if len(self.queue) >= self.cap:
                self.queue.remove(len(self.queue) - 1)
            self.queue.appendleft(new_node)
            self.hashmap[0] = new_node