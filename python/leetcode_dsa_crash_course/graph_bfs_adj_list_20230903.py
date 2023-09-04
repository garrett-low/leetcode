from collections import deque

def bfs(graph, start, end):
    prev = {}
    seen = set(start)
    prev[start] = None
    
    queue = deque(start)
    while len(queue) > 0:
        curr = queue.popleft()
        
        neighbors = graph.adj_list[curr]
        for neighbor in neighbors:
            if neighbor in seen:
                continue
            
            queue.append(neighbor)
            seen.add(neighbor)
            prev[neighbor] = curr
    
    if not prev[end]:
        print([])
        return
    
    output_path = deque(end)
    curr = prev[end]
    while curr:
        output_path.appendleft(curr)
        curr = prev[curr]
    
    print(output_path)
    return

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
                val = [neighbor.strip() for neighbor in colon_split[1].split(',')]
                self.adj_list[key] = val
    
    def __str__(self):
        retval = ""
        for key in self.adj_list:
            retval += f"{key}: {self.adj_list[key]}\n"
        return retval

def main():
    matrix1 = adj_list('graph_dfs_input_adj_list.txt')
    print(matrix1)
    bfs(matrix1, 'A', 'E')
    
if __name__ == "__main__":
    main()