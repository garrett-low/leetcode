import math
from adj_list_weighted import adj_list
from min_heap_node import min_heap

# dijkstra's with adjacency list
# wikipedia pseudocode
def dijkstra(adj_list):
    unvisited_min_heap = min_heap()
    dist_dict = dict()
    prev_dict = dict()
    
    dist_dict['A'] = 0 # starting node as A
    
    for vertex in adj_list.adj_list.keys():
        if vertex != 'A':
            dist_dict[vertex] = math.inf
            prev_dict[vertex] = None
        unvisited_min_heap.add(vertex, dist_dict[vertex])
    print(f"starting distances: {dist_dict}")
    print(f"starting nearest parent: {prev_dict}")
    print(f"starting min heap: {unvisited_min_heap}")
    
    while len(unvisited_min_heap) > 0:
        curr_element = unvisited_min_heap.remove()
        
        edge_list = adj_list.adj_list[curr_element]
        print(f"visit: {curr_element}")
        for edge in edge_list:
            test_dist = dist_dict[curr_element] + edge.weight
            
            if test_dist < dist_dict[edge.to]:
                dist_dict[edge.to] = test_dist
                prev_dict[edge.to] = curr_element
                print(f"update shortest path --> {edge.to}: {test_dist}")
                unvisited_min_heap.update(curr_element, test_dist)
    
    return dist_dict, prev_dict

def main():
    graph = adj_list('input_list_weighted.txt')
#     print(graph)
    print(dijkstra(graph))
    
if __name__ == "__main__":
    main()