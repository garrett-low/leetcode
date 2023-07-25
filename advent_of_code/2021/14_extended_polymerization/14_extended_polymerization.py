import sys

def polymer(filename, num_steps = 10):
    template = ""
    pair_insert_dict = {}
    with open(filename, 'rt', encoding = 'utf-8') as file:
        template = file.readline().strip()
        file.readline() # blank empty second line
        for line in file:
            line_split = line.strip().split(' -> ')
            output = line_split[1]
            input_tuple = (line_split[0][0], line_split[0][1])
            pair_insert_dict[input_tuple] = output
            
#     debug_input(template, pair_insert_dict)
    polymer_pairs = {}
    first_pair_tuple = (template[0], template[1])
#     last_pair_tuple = (template[len(template) - 2], template[len(template) - 1])
    for i in range(len(template) - 1):
        pair_tuple = (template[i], template[i + 1])
        if pair_tuple not in polymer_pairs:
            polymer_pairs[pair_tuple] = 1
        else:
            polymer_pairs[pair_tuple] += 1
    
#     debug_rejoin_pairs(polymer_pairs, 0)
#     print(polymer_pairs)
#     print(first_pair_tuple)
#     print(last_pair_tuple)

    for step_i in range(num_steps):
        new_polymer_pairs = {}
        is_first_pair_tuple_updated = False
#         is_last_pair_tuple_updated = False
        for pair_tuple in polymer_pairs:
            output = pair_insert_dict[pair_tuple]
            first_half, second_half = pair_tuple
            first_new_tuple = (first_half, output)
            second_new_tuple = (output, second_half)
            count_original_pair = polymer_pairs[pair_tuple]
            
            if pair_tuple == first_pair_tuple and not is_first_pair_tuple_updated:
                first_pair_tuple = first_new_tuple
                is_first_pair_tuple_updated = True
#             elif pair_tuple == last_pair_tuple and not is_last_pair_tuple_updated:
#                 last_pair_tuple = second_new_tuple
#                 is_last_pair_tuple_updated = True

            if first_new_tuple not in new_polymer_pairs:
                new_polymer_pairs[first_new_tuple] = count_original_pair
            else:
                new_polymer_pairs[first_new_tuple] += count_original_pair
            
            if second_new_tuple not in new_polymer_pairs:
                new_polymer_pairs[second_new_tuple] = count_original_pair
            else:
                new_polymer_pairs[second_new_tuple] += count_original_pair
        
        polymer_pairs = new_polymer_pairs
#         print(polymer_pairs)
#         print(first_pair_tuple)
#         print(last_pair_tuple)
#         count_elements = get_count_elements(polymer_pairs, first_pair_tuple)
#         print(count_elements)
#         debug_rejoin_pairs(polymer_pairs, step_i + 1)
    
    # OUTPUT
    count_elements = get_count_elements(polymer_pairs, first_pair_tuple)
    print(count_elements)
    
    min_ele_count = sys.maxsize
    max_ele_count = 0
    min_ele = ""
    max_ele = ""
    for element in count_elements:
        count = count_elements[element]
        if count < min_ele_count:
            min_ele_count = count
            min_ele = element
        if count > max_ele_count:
            max_ele_count = count
            max_ele = element
    
    part_one_output = max_ele_count - min_ele_count
    print(part_one_output)
    return

def get_count_elements(polymer_pairs, first_pair_tuple):
    count_elements = {}
    for pair_tuple in polymer_pairs:
        first_half, second_half = pair_tuple
        count_pairs = polymer_pairs[pair_tuple]
#         
#         if first_half not in count_elements:
#             count_elements[first_half] = count_pairs
#         else:
#             count_elements[first_half] += count_pairs
        
        if second_half not in count_elements:
            count_elements[second_half] = count_pairs
        else:
            count_elements[second_half] += count_pairs
    
    count_pairs = polymer_pairs[first_pair_tuple]
    if first_pair_tuple[0] not in count_elements:
        count_elements[first_pair_tuple[0]] = 1
    else:
        count_elements[first_pair_tuple[0]] += 1
    
    return count_elements
    
def debug_rejoin_pairs(polymer_pairs, step_i):
#     print(polymer_pairs)
    polymer_out = ""
    for i in range(len(polymer_pairs)):
        first_half, second_half = polymer_pairs[i]
        if i == 0:
            polymer_out += first_half
            polymer_out += second_half
        else:
            polymer_out += second_half
    print(f"STEP {step_i}: {polymer_out}")
    return polymer_out

def debug_input(template, pair_insert_dict):
    print(template)
    for input_tuple in pair_insert_dict:
        print(f"{input_tuple} -> {pair_insert_dict[input_tuple]}")

polymer('sample.txt')
polymer('input.txt')
# my answer for p1 is 2345

# PART TWO
polymer('sample.txt', 40)
polymer('input.txt', 40)