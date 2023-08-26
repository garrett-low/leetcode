# from enum import Enum
from collections import deque

def carry_this_bag(filename, target_color):
    bag_list = []
    # P1
    inner_to_outer_dict = {} # key = inner or child bag, 
                             # val = set of outer or parent bags
    # P2
    outer_to_inner_dict = {} # key = outer/parent bag
                             # val = set of inner bags;
                             #       each item is a tuple of quantity + color
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            bag_contains_split = line.strip().split(' bags contain ')
        
            outer_bag = bag_contains_split[0]
            
            # P2
            if bag_contains_split[1] == "no other bags.":
                if outer_bag not in outer_to_inner_dict:
                    outer_to_inner_dict[outer_bag] = set()
                continue
            
            inner_bags_string_split = bag_contains_split[1].split(' ')
            for i, curr_string in enumerate(inner_bags_string_split):
                if i % 4 == 0:
                    inner_bag_ct = int(curr_string)
                elif i % 4 == 1:
                    inner_bag_adjective = curr_string
                elif i % 4 == 2:
                    inner_bag_color = curr_string
                elif i % 4 == 3:
                    # print("  ", inner_bag_adjective, inner_bag_color, inner_bag_ct)
                    inner_bag = inner_bag_adjective + " " + inner_bag_color
                    # P1
                    if inner_bag not in inner_to_outer_dict:
                        inner_to_outer_dict[inner_bag] = set()
                    inner_to_outer_dict[inner_bag].add(outer_bag)
                    
                    # P2
                    if outer_bag not in outer_to_inner_dict: # p2
                        outer_to_inner_dict[outer_bag] = set()
                    outer_to_inner_dict[outer_bag].add((inner_bag_ct, inner_bag))
                    
    
    # debug stuff for p1
    # for inner_bag in inner_to_outer_dict:
        # print(inner_bag)
        # for outer_bag in inner_to_outer_dict[inner_bag]:
            # print("  " + outer_bag)
    
    parent_bags = p1_bfs(inner_to_outer_dict, target_color)
    print("P1 parent bag colors: ", len(parent_bags))
    print("    ", parent_bags)
    
    # debug stuff for P2
    # for outer_bag in outer_to_inner_dict:
        # print(outer_bag)
        # for inner_bag in outer_to_inner_dict[outer_bag]:
            # print(f"  {inner_bag[0]} {inner_bag[1]}")
    child_bag_list = []
    visited_set = set()
    start_bag = (1, target_color)
    parent_bag_ct = 1
    p2_dfs(outer_to_inner_dict, start_bag, child_bag_list, visited_set, parent_bag_ct)
    child_bag_total = 0
    for i in range(1, len(child_bag_list)): # skip 0 for skipping start color
        child_bag_ct, child_bag_color, parent_ct = child_bag_list[i]
        child_bag_total += child_bag_ct * parent_ct
    print("P2 total child bag count: ", child_bag_total)
    print("    ", child_bag_list)

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

def p2_dfs(adj_list, curr, path, visited_set, parent_ct):
    curr_ct, curr_color = curr
    if curr_color in visited_set:
        return
    
    visited_set.add(curr)
    path.append((curr_ct, curr_color, parent_ct))
    for neighbor in adj_list[curr_color]:
        # neighbor_ct, neighbor_color = neighbor
        p2_dfs(adj_list, neighbor, path, visited_set, curr_ct * parent_ct)
    
    return
    
carry_this_bag('sample.txt', 'shiny gold')
carry_this_bag('sample2.txt', 'shiny gold')
carry_this_bag('input.txt', 'shiny gold')
# p1 = 128