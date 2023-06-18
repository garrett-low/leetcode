from adj_list_unweighted import adj_list

# return the DFS path to the node
# else return empty list
def dfs(graph, val):
    seen = set()
    path = ['A'] # let's just say A is starting node
    curr = 'A'
    is_found = dfs_inner(graph, curr, val, path, seen)
    if is_found:
        return path
    return []

def dfs_inner(graph, curr, val, path, seen):
    if curr == val:
        return True
    if curr in seen:
        return False
    
    seen.add(curr)
    
    for neighbor in graph.adj_list[curr]:
        path.append(neighbor)
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