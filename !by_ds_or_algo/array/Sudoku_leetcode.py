class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        row_set = [set() for _ in range(len(board[0]))]
        col_set = [set() for _ in range(len(board[0]))]
        subbox_set = [set() for _ in range(len(board[0]))]
        
        for row_idx, row in enumerate(board):
            for col_idx, cell_val in enumerate(row):
                if cell_val == ".":
                    continue
                
                if cell_val in row_set[row_idx]:
                    print(cell_val)
                    return False
                row_set[row_idx].add(cell_val)
                
                if cell_val in col_set[col_idx]:
                    print(cell_val)
                    return False
                col_set[col_idx].add(cell_val)
                
                box_idx = ((row_idx // 3) * 3) + col_idx // 3
                if cell_val in subbox_set[box_idx]:
                    print(cell_val)
                    return False
                subbox_set[box_idx].add(cell_val)
            
        return True
        
        """
        for row in board:
            for i in row:
                print(i, end=' ')
            print("\n")
            
        for i in range(len(board[0])):
            for j in board[i]:
                print(j,  end=' ')
            print("\n")
        """

matrix = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

print(matrix)

x = Solution()
print(x.isValidSudoku(matrix))