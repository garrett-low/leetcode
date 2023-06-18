# adj_matrix for integer vertices
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
    matrix1 = matrix('input.txt')
    print(matrix1)
    
if __name__ == "__main__":
    main()