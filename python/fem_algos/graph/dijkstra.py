from collections import deque
import sys
from adj_list_weighted import adj_list
from min_heap_node import min_heap

# dijkstra's with adjacency list
# wikipedia pseudocode
def dijkstra(graph):
    unvisited_min_heap = min_heap()
    dist_dict = dict()
    prev_dict = dict()
    
    dist_dict['A'] = 0 # starting node as A
    
    for vertex in graph.adj_list.keys():
        if vertex != 'A':
            dist_dict[vertex] = sys.maxsize
            prev_dict[vertex] = None
        unvisited_min_heap.add(vertex, dist_dict[vertex])
    print(f"starting distances: {dist_dict}")
    print(f"starting nearest parent: {prev_dict}")
    print(f"starting min heap: {unvisited_min_heap}")
    
    while len(unvisited_min_heap) > 0:
        curr_element = unvisited_min_heap.remove()
        
        edge_list = graph.adj_list[curr_element]
        print(f"visit: {curr_element}")
        for edge in edge_list:
            test_dist = dist_dict[curr_element] + edge.weight
            
            if test_dist < dist_dict[edge.to]:
                dist_dict[edge.to] = test_dist
                prev_dict[edge.to] = curr_element
                print(f" * update shortest path --> {edge.to}: {test_dist}")
                unvisited_min_heap.update(edge.to, test_dist)
    
    return dist_dict, prev_dict

def dijkstra_path_to(graph, needle):
    unvisited_min_heap = min_heap()
    dist_dict = dict()
    prev_dict = dict()
    
    dist_dict['A'] = 0 # starting node as A
    
    for vertex in graph.adj_list.keys():
        if vertex != 'A':
            dist_dict[vertex] = sys.maxsize
        prev_dict[vertex] = None
        unvisited_min_heap.add(vertex, dist_dict[vertex])
    print(f"starting distances: {dist_dict}")
    print(f"starting nearest parent: {prev_dict}")
    print(f"starting min heap: {unvisited_min_heap}")
    
    while len(unvisited_min_heap) > 0:
        curr_element = unvisited_min_heap.remove()
        
        edge_list = graph.adj_list[curr_element]
        print(f"visit: {curr_element}")
        for edge in edge_list:
            test_dist = dist_dict[curr_element] + edge.weight
            
            if test_dist < dist_dict[edge.to]:
                dist_dict[edge.to] = test_dist
                prev_dict[edge.to] = curr_element
                print(f" * update shortest path --> {edge.to}: {test_dist}")
                unvisited_min_heap.update(edge.to, test_dist)
    
    out_path = deque([needle])
    curr_parent = prev_dict[needle]
    while curr_parent != None:
        out_path.appendleft(curr_parent)
        curr_parent = prev_dict[curr_parent]
    
    return out_path

def main():
    # example from https://www.youtube.com/watch?v=_lHSawdgXpI
    graph = adj_list('input_list_weighted.txt')
#     print(graph)
    print(dijkstra(graph))
    print(f"shortest path to E: {dijkstra_path_to(graph, 'E')}")
    
if __name__ == "__main__":
    main()