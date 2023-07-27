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

def dfs_inner(adj, curr, small_cave_set, path, visited, has_visited_small_twice):
    count_path = 0
#     if curr in visited and visited[curr] == 2:
# #         has_visited_small_twice = True
#         return count_path, True, curr
#     if has_visited_small_twice and curr in visited:
#         return count_path, has_visited_small_twice, small_cave_twice_visited
#     if curr in visited and (curr == 'start' or curr == 'end'):
#         return count_path, has_visited_small_twice, small_cave_twice_visited
    if curr == END:
#         if curr not in visited:
#             visited[curr] = 1
#         else:
#             visited[curr] += 1
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
    
#     if curr.islower():
#         if curr not in visited:
#             visited[curr] = 1
#         else:
#             visited[curr] += 1
    path.append(curr)
#     print(f"VISITING: {curr}, {visited}, {path}")
    
#     if curr == end_val:
# #         print(path)
#         count_path += 1
    count_path = 0
    for neighbor in adj[curr]:
#         print(f"\tNEIGHBOR: {neighbor}")
        if neighbor == START:
            continue
        count_path += dfs_inner(adj, neighbor, small_cave_set, path, visited, has_visited_small_twice)
    
    if curr in small_cave_set:
        if curr in visited and visited[curr] > 0:
            visited[curr] -= 1
#     if curr.islower():
#         if visited[curr] > 1:
#             visited[curr] -= 1
#         else:
#             visited.pop(curr)
#         if curr == small_cave_twice_visited:
#             has_visited_small_twice = False
#             small_cave_twice_visited = ""
    
    path.pop()
    return count_path

dfs('sample.txt')
dfs('sample2.txt')
dfs('sample3.txt')
dfs('input.txt')
