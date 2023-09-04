from collections import deque

def bfs(graph, start, end):
    prev = [-1] * len(graph.matrix[0])
    seen = [False] * len(graph.matrix[0])

    seen[0] = True
    queue = deque([start])
    
    while len(queue) > 0:
        curr = queue.popleft()
        neighbor_row = graph.matrix[curr]
        
        for neighbor_i in range(len(neighbor_row)):
            neighbor_weight = neighbor_row[neighbor_i]
            if neighbor_weight <= 0:
                continue
            if seen[neighbor_i]:
                continue
            
            seen[neighbor_i] = True
            queue.append(neighbor_i)
            prev[neighbor_i] = curr
    
    if prev[end] == -1:
        print("Couldn't find!")
        return
    
    path = deque([end])
    curr = prev[end]
    while curr != -1:
        path.appendleft(curr)
        curr = prev[curr]
    
    print(path)

class matrix:
    def __init__(self, filename):
        self.matrix = []
        with open(filename, 'rt', encoding='utf-8') as file:
            for line in file:
                self.matrix.append(list(map(int, line.strip().split(','))))
    
    def __str__(self):
        retval = ""
        height = range(len(self.matrix))
        width = range(len(self.matrix[0]))
        for row in height:
            for col in width:
                retval += f"{self.matrix[row][col]} "
            retval += "\n\n"
        return retval

def main():
    matrix1 = matrix('graph_bfs_input.txt')
    print(matrix1)
    bfs(matrix1, 0, 4)
    
if __name__ == "__main__":
    main()