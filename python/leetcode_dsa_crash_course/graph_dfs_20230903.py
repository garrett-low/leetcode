def dfs(graph, start, end):
    out_path = []
    seen = set()
    dfs_inner(graph, start, end, seen, out_path)
    print(out_path)
    return out_path

def dfs_inner(graph, curr, end, seen, out_path):
    if curr in seen:
        return False
    
    out_path.append(curr)
    seen.add(curr)
    
    if curr == end:
        return True
    
    neighbors = graph.adj_list[curr]
    for neighbor in neighbors:
        if dfs_inner(graph, neighbor, end, seen, out_path):
            return True
    
    out_path.pop()
    
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
                val = [neighbor.strip() for neighbor in colon_split[1].split(',')]
                self.adj_list[key] = val
    
    def __str__(self):
        retval = ""
        for key in self.adj_list:
            retval += f"{key}: {self.adj_list[key]}\n"
        return retval

def main():
    matrix1 = adj_list('input_list.txt')
    print(matrix1)
    dfs(matrix1, 'A', 'E')
    
if __name__ == "__main__":
    main()