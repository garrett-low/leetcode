class edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight
    def __str__(self):
        return f"[{self.to}: {self.weight}]"

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
                if len(colon_split) <= 1:
                    continue
                
                edge_list = []
                edge_split = colon_split[1].split(',')
                for item in edge_split:
                    item = item.strip()
                    item_split = item.split('-')
                    if len(item_split) <= 1:
                        continue
                    new_edge = edge(item_split[0], int(item_split[1]))
                    edge_list.append(new_edge)
                
                self.adj_list[key] = edge_list
    
    def __str__(self):
        retval = ""
        for key in self.adj_list:
            retval += f"{key}: "
            for curr_edge in self.adj_list[key]:
                retval += f"{curr_edge}"
            retval += "\n"
        return retval

def main():
    matrix1 = adj_list('input_list_weighted.txt')
    print(matrix1)
    
if __name__ == "__main__":
    main()