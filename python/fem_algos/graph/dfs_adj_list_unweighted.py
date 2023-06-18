from adj_list_unweighted import adj_list

# time complexity: O(V + E) - check every vertex and edge in worst case
# return the DFS path to the node
# else return empty list
def dfs(graph, val):
    path = []
    seen = set()
    curr = 'A' # let's just say A is starting node
    is_found = dfs_inner(graph, curr, val, path, seen)
    if is_found:
        return path
    return []

def dfs_inner(graph, curr, val, path, seen):
    if curr in seen:
        return False
    
    seen.add(curr)
    path.append(curr)
    if curr == val:
        return True
    
    for neighbor in graph.adj_list[curr]:
        if dfs_inner(graph, neighbor, val, path, seen):
            return True
    
    path.pop()
    return False

def main():
    graph1 = adj_list('input_list.txt')
    print(graph1)
    print(dfs(graph1, 'E'))
    
if __name__ == "__main__":
    main()