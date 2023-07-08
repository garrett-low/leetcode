from collections import deque
import sys
from adj_list_weighted import adj_list
from min_heap_node import min_heap

# class edge:
#     def __init__(self, to, weight):
#         self.to = to
#         self.weight = weight
#     def __str__(self):
#         return f"[{self.to}: {self.weight}]"

def dijkstra(filename, to_node = None):
    unvisited_min_heap = min_heap()
    dist_dict = {}
    prev_dict = {}
    
    graph = adj_list(filename)
        
    dist_dict['A'] = 0
    for node in graph.adj_list.keys():
        if node != 'A':
            dist_dict[node] = sys.maxsize
        prev_dict[node] = None
        unvisited_min_heap.add(node, dist_dict[node])
    
    while not unvisited_min_heap.is_empty():
        curr_node = unvisited_min_heap.remove()
        for neighbor in graph.adj_list[curr_node]:
            old_dist = dist_dict[neighbor.to]
            test_dist = dist_dict[curr_node] + neighbor.weight
            if old_dist > test_dist:
                prev_dict[neighbor.to] = curr_node
                dist_dict[neighbor.to] = test_dist
    
    if to_node == None:
        print(prev_dict)
        print(dist_dict)
    else:
        curr_node = prev_dict[to_node]
        output = deque(to_node)
        while curr_node != None:
            output.appendleft(curr_node)
            curr_node = prev_dict[curr_node]
        print(output)
    return
    
def dict_syntax():
    dict1 = {}
    dict1.update({'A': 'Z'})
    dict1.update({'B': 'Y'})
    print(dict1)
    
dijkstra('input_list_weighted.txt')
dijkstra('input_list_weighted.txt', 'E')