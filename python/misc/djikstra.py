import heapq
from collections import deque
import sys

def djikstra(graph, start, end):
    prev_dict = {}
    dist_dict = {}
    unvisited_min_heap = []
    
    # initial state
    # start node is given dist 0
    # all others infinite
    dist_dict[start] = 0
    for vertex in graph.adj_list:
        if vertex != 'A':
            dist_dict[vertex] = sys.maxsize
        prev_dict[vertex] = None
        
        # priority val is the distance to the vertex, val is the vertex itself
        heapq.heappush(unvisited_min_heap, (dist_dict[vertex], vertex))
    
    # print(dist_dict)
    # print(prev_dict)
    # print(unvisited_min_heap)
    
    while len(unvisited_min_heap) > 0:
        dist, curr = heapq.heappop(unvisited_min_heap)
        
        neighbors = graph.adj_list[curr]
        for neighbor in neighbors:
            # if the distance from curr to neighbor is less than what we have currently
            test_dist = neighbor.weight + dist_dict[curr]
            curr_dist_to_neighbor = dist_dict[neighbor.to]
            if test_dist < curr_dist_to_neighbor:
                heapq_update(unvisited_min_heap, neighbor.to, curr_dist_to_neighbor, test_dist)
                dist_dict[neighbor.to] = test_dist
                prev_dict[neighbor.to] = curr
    
    if prev_dict[end] == None:
        print("no path!")
        return deque()
    
    output_path = deque(end)
    curr = prev_dict[end]
    
    while curr:
        output_path.appendleft(curr)
        curr = prev_dict[curr]
    
    print(output_path)
    return output_path

def heapq_update(min_heap, curr, old_prio, new_prio):
    # there are better heap structures for heap update
    # print(min_heap)
    # print(old_prio, curr)
    min_heap.remove((old_prio, curr))
    min_heap.append((new_prio, curr))
    heapq.heapify(min_heap)
    
class edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight
    def __str__(self):
        return f"[{self.to}: {self.weight}]"

#adj list graph without weights
class adj_list:
    def __init__(self, filename):
        # use dictionary for adjacency list
        # where dict key is the node value
        # and the dict val is the adjacent nodes
        self.adj_list = {}
        with open(filename, 'rt', encoding = 'utf-8') as file:
            for line in file:
                colon_split = line.split(':')
                key = colon_split[0].strip()
                if len(colon_split) <= 1:
                    continue
                
                edge_list = []
                edge_split = colon_split[1].split(',')
                for item in edge_split:
                    item = item.strip()
                    item_split = item.split('-')
                    if len(item_split) <= 1:
                        continue
                    new_edge = edge(item_split[0], int(item_split[1]))
                    edge_list.append(new_edge)
                
                self.adj_list[key] = edge_list
    
    def __str__(self):
        retval = ""
        for key in self.adj_list:
            retval += f"{key}: "
            for curr_edge in self.adj_list[key]:
                retval += f"{curr_edge}"
            retval += "\n"
        return retval

def main():
    matrix1 = adj_list('input_list_weighted.txt')
    print(matrix1)
    djikstra(matrix1, 'A', 'E')
    
if __name__ == "__main__":
    main()