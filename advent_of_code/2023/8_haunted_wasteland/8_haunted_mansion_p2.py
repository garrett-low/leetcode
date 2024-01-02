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
    instr_length = len(instruct_string)
    # curr_node_list = []
    step_count_list = []
    for this_val in tree.lookup_dict:
        if this_val[2] != START_VAL:
            continue
        
        # curr_node_list.append(tree.lookup_dict[this_val][0])
        
        curr_node = tree.lookup_dict[this_val][0]
        i = 0
        
        while True:
            # print(curr_node)
            if curr_node.val[2] == END_VAL:
                break
                
            instruction = instruct_string[i % instr_length]
            
            if instruction == 'L':
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
            
            i += 1
            
        # print(i)
        step_count_list.append(i)
    
    # result = 1
    # for step_count in step_count_list:
        # result *= step_count
    # print(result)
    
    lcm_result = lcm(step_count_list[0], step_count_list[1])
    for i in range(2, len(step_count_list)):
        # print(lcm_result)
        lcm_result = lcm(lcm_result, step_count_list[i])
    print(lcm_result)

def gcd(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1

def lcm(num1, num2):
    this_gcd = gcd(num1, num2)
    return (num1 * num2) // this_gcd

haunted('sample_p2.txt')
haunted('input.txt') # is this LCM? 49153966541198323241619811 too high
# attempt #2 with actually calculating LCM: 269024535019
# attempt #3 18024643846273 with correct lcm_result
# print(gcd(252, 105))
# print(gcd(105, 252))
# print(lcm(252, 105))
# print(lcm(105, 252))