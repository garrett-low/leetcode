from collections import deque
import sys
from adj_list_weighted import adj_list
from min_heap_node import min_heap

def dijkstra(filename, dest):
    graph = adj_list(filename)
    
    unvisited_min_heap = min_heap()
    prev_dict = {}
    dist_dict = {}
    dist_dict['A'] = 0
    for vertex in graph.adj_list:
        if vertex != 'A':
            dist_dict[vertex] = sys.maxsize
        prev_dict[vertex] = None
        unvisited_min_heap.add(vertex, dist_dict[vertex])
    
    while not unvisited_min_heap.is_empty():
        visit = unvisited_min_heap.remove()
        
        for neighbor in graph.adj_list[visit]:
            test_dist = neighbor.weight + dist_dict[visit]
            if test_dist < dist_dict[neighbor.to]:
                dist_dict[neighbor.to] = test_dist
                prev_dict[neighbor.to] = visit
    
    print(prev_dict)
    print(dist_dict)
    
    path = deque([dest])
    prev = prev_dict[dest]
    while prev != None:
        path.appendleft(prev)
        prev = prev_dict[prev]
    
    print(path)

dijkstra('input_list_weighted.txt', 'E')