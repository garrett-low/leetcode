class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        string = f"{self.val} = ({self.left.val}, {self.right.val})"
        return string
    
class Tree:
    def __init__(self):
        self.lookup_dict = {}
    
    def __str__(self):
        string = ""
        for node in self.lookup_dict:
            string += f"{node}\n"
        return string

START_VAL = "A"
END_VAL = "Z"

def haunted(filename):
    instruct_string = ""
    tree = Tree()
    with open(filename, 'rt') as file:
        instruct_string = file.readline().strip()
        file.readline()
        
        # rest of file are leaves
        for line in file:
            this_val = ""
            this_left = ""
            this_right = ""
            
            line_split = line.strip().split('=')
            this_val = line_split[0].strip()
            
            child_split = line_split[1].split(',')
            this_left = child_split[0][2:]
            this_right = child_split[1][1:4]
            # print(this_val, this_left, this_right)
            
            node = Node(this_val)
            tree.lookup_dict[this_val] = (node, this_left, this_right)
    
    # build node left and node right
    for this_val in tree.lookup_dict:
        this_node, left_val, right_val = tree.lookup_dict[this_val]
        left_node = tree.lookup_dict[left_val][0]
        right_node = tree.lookup_dict[right_val][0]
        this_node.left = left_node
        this_node.right = right_node
        
    # done = False
    instr_length = len(instruct_string)
    i = 0
    
    # P2 also build starting node (nodes that end in A)
    curr_node_list = []
    for this_val in tree.lookup_dict:
        if this_val[2] != START_VAL:
            continue
        
        curr_node_list.append(tree.lookup_dict[this_val][0])
    
    while True:
        is_all_node_end = True
        for curr_node in curr_node_list:
            if curr_node.val[2] != END_VAL:
                is_all_node_end = False
                break
        
        if is_all_node_end:
            break
            
        # print(curr_node)
            
        instruction = instruct_string[i % instr_length]
        
        new_node_list = []
        for curr_node in curr_node_list:
            if instruction == 'L':
                new_node = curr_node.left
            else:
                new_node = curr_node.right
            
            new_node_list.append(new_node)
        
        curr_node_list = new_node_list
        i += 1
        
    print(i)
haunted('sample_p2.txt')
haunted('input.txt')