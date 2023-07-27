START = 'start'
END = 'end'

def dfs(filename):
    adj = {} # adjacency matrix unweighted
    small_cave_set = set()
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            split = line.strip().split('-')
            from_node = split[0]
            to_node = split[1]
            
            if from_node not in adj:
                adj[from_node] = set([to_node])
            else:
                adj[from_node].add(to_node)
            
            if to_node not in adj:
                adj[to_node] = set([from_node])
            else:
                adj[to_node].add(from_node)
            
            if from_node.islower():
                small_cave_set.add(from_node)
            if to_node.islower():
                small_cave_set.add(to_node)
#     print(adj)
    
    visited = {}
    path = []
    count = dfs_inner(adj, START, small_cave_set, path, visited, False)
    print(count)
    
def dfs_inner(adj, curr, small_cave_set, path, visited, has_visited_small_twice):
    count_path = 0
    if curr == END:
        path.append(curr)
#         print(path)
        path.pop()
        return 1
    
    if curr in visited and visited[curr] > 0 and has_visited_small_twice:
        return 0
    
    if curr in small_cave_set:
        if curr not in visited:
            visited[curr] = 1
        else:
            visited[curr] += 1
        if visited[curr] == 2:
            has_visited_small_twice = True
    
    path.append(curr)
    
    count_path = 0
    for neighbor in adj[curr]:
        if neighbor == START:
            continue
        count_path += dfs_inner(adj, neighbor, small_cave_set, path, visited, has_visited_small_twice)
    
    if curr in small_cave_set:
        if curr in visited and visited[curr] > 0:
            visited[curr] -= 1
    
    path.pop()
    return count_path

dfs('sample.txt')
dfs('sample2.txt')
dfs('sample3.txt')
dfs('input.txt')