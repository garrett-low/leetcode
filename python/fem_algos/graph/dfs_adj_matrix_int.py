from adj_matrix_int import matrix
from collections import deque

# dfs on integer adjacency matrix
# returns path from 0 node to val
def dfs(matrix, val):
    length = len(matrix.matrix[0])
    
    prev = [-1] * length
    seen = [False] * length
    seen[0] = True
    queue = deque([0])
    
    while len(queue) > 0:
        curr = queue.popleft()
        
        if curr == val:
            break
        
        for edge in range(length):
            if matrix.matrix[curr][edge] <= 0: # not an edge in the integer adj matrix
                continue
            if seen[edge]:
                continue
            
            seen[edge] = True
            prev[edge] = curr
            queue.append(edge)
    
    if prev[val] == -1:
        return []
    
    # build path from prev list
    curr = val
    path = deque()
    while prev[curr] != -1:
        path.appendleft(curr)
        curr = prev[curr]
    path.appendleft(0) # 0 was start
    
#     print(prev)
#     print(seen)
    
    return path

def main():
    matrix1 = matrix('input.txt')
    print(matrix1)
    print(dfs(matrix1, 4))
#     matrix2 = matrix('input2.txt')
#     print(matrix2)
#     print(dfs(matrix2, 4))
    
if __name__ == "__main__":
    main()