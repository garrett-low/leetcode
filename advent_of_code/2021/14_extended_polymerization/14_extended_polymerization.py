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
    polymer_pairs = []
    for i in range(len(template) - 1):
        polymer_pairs.append((template[i], template[i + 1]))
    
#     debug_rejoin_pairs(polymer_pairs, 0)
    
    for step_i in range(num_steps):
        new_polymer = []
        for pair_tuple in polymer_pairs:
            output = pair_insert_dict[pair_tuple]
            first_half, second_half = pair_tuple
            new_polymer.append((first_half, output))
            new_polymer.append((output, second_half))
        polymer_pairs = new_polymer
#         debug_rejoin_pairs(polymer_pairs, step_i + 1)
    
    # PART ONE OUTPUT
    count_elements = {}
    for i in range(len(polymer_pairs)):
        first_half, second_half = polymer_pairs[i]
        if i == 0:
            count_elements[first_half] = 1
            count_elements[second_half] = 1
        else:
            if second_half not in count_elements:
                count_elements[second_half] = 1
            else:
                count_elements[second_half] += 1
#     print(count_elements)
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