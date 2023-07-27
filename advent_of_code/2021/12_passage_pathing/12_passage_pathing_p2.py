def dfs(filename):
    adj = {} # adjacency matrix unweighted
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
    
#     print(adj)
    
    visited = {}
    path = []
    count = dfs_inner(adj, 'start', 'end', path, visited)
    print(count)
#     print(path)
    
#     visited.add('start')
#     stack.append('start')
#     
#     while len(stack) > 0:
#         curr = stack.pop()
#         print(curr, end = " ")
#         
#         for neighbor in adj[curr]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 stack.append(neighbor)

def dfs_inner(adj, curr, end_val, path, visited):
    count_path = 0
    if curr in visited and visited[curr] == 2:
        return count_path
    if curr in visited and (curr == 'start' or curr == 'end'):
        return count_path

    if curr.islower():
        if curr not in visited:
            visited[curr] = 1
        else:
            visited[curr] += 1
    path.append(curr)
#     print(f"VISITING: {curr}, {visited}, {path}")
    
    if curr == end_val:
        print(path)
        count_path += 1

    for neighbor in adj[curr]:
#         print(f"\tNEIGHBOR: {neighbor}")
        count_path += dfs_inner(adj, neighbor, end_val, path, visited)
    
    if curr.islower():
        if visited[curr] > 1:
            visited[curr] -= 1
        else:
            visited.pop(curr)
    
    path.pop()
    return count_path

dfs('sample.txt')
# dfs('sample2.txt')
# dfs('sample3.txt')
# dfs('input.txt')