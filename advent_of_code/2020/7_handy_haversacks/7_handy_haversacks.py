# from enum import Enum
from collections import deque

class bag:
    def __init__(self, color, bag_dict = {}):
        self.color = color
        self.bag_dict = bag_dict
    def __str__(self):
        retval = ""
        retval += f"{self.color} bag: "
        for inner_bag in self.bag_dict:
            inner_bag_ct = self.bag_dict[inner_bag]
            retval += f"  {inner_bag_ct}: {inner_bag}"
        retval += "\n"
        return retval

def carry_this_bag(filename, target_color):
    bag_list = []
    inner_to_outer_dict = {} # key = inner or child bag, 
                        # val = set of outer or parent bags
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            bag_contains_split = line.strip().split(' bags contain ')
        
            outer_bag = bag_contains_split[0]
            # print(outer_bag)
            # inner_bags_string = bag_contains_split[1]
            # if bag_contains_split[0]:
            
            inner_bags_string_split = bag_contains_split[1].split(' ')
            for i, curr_string in enumerate(inner_bags_string_split):
                if i % 4 == 0:
                    inner_bag_ct = curr_string
                elif i % 4 == 1:
                    inner_bag_adjective = curr_string
                elif i % 4 == 2:
                    inner_bag_color = curr_string
                elif i % 4 == 3:
                    # print("  ", inner_bag_adjective, inner_bag_color, inner_bag_ct)
                    inner_bag = inner_bag_adjective + " " + inner_bag_color
                    if inner_bag not in inner_to_outer_dict:
                        inner_to_outer_dict[inner_bag] = set()
                    
                    inner_to_outer_dict[inner_bag].add(outer_bag)
    
    # debug stuff
    # for inner_bag in inner_to_outer_dict:
        # print(inner_bag)
        # for outer_bag in inner_to_outer_dict[inner_bag]:
            # print("  " + outer_bag)
    
    parent_bags = p1_bfs(inner_to_outer_dict, target_color)
    print(parent_bags)
    print(len(parent_bags))

def p1_bfs(adj_list, start):
    q = deque()
    q.append(start)
    parent_bags = set()
    
    while len(q) > 0:
        curr = q.popleft()
        
        if curr not in adj_list:
            continue
        
        adj_set = adj_list[curr]
        for neighbor in adj_set:
            q.append(neighbor)
            parent_bags.add(neighbor)
    
    return parent_bags
    
carry_this_bag('sample.txt', 'shiny gold')
carry_this_bag('input.txt', 'shiny gold')
# p1 = 128